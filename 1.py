
#스파게티 코드, 다 같이 풀어봐요
#51번째 줄 추가
#103번째 줄 for loop 변경
# 166번째 줄 for loop 변경
# 163번째 줄 collision 추가
# 63번쨰 줄 random모듈 사용 추가


import pygame
import random
import math

#파이게임 초기화
pygame.init()

#게임 창 설정
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Brick Break Game")

#색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

#패들 사각형 설정
paddle_width = 100
paddle_height = 10
paddle_x = window_width // 2 - paddle_width // 2
paddle_y = window_height - paddle_height - 10
paddle_movement = 5
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

#공 변수 설정
#ball_angle 에서 exept 0(rad) 추가
if random.uniform(-math.pi / 4, math.pi / 4) == 0:
    ball_angle = random.uniform(-math.pi / 4, math.pi / 4)
ball_radius = 10
ball_x = window_width // 2
ball_y = window_height // 2
ball_speed = 4
# ball_angle = random.uniform(-math.pi / 4, math.pi / 4)  #30도에서 60도 사이의 임의 초기 각도
ball_dx = ball_speed * math.cos(ball_angle)
ball_dy = -ball_speed * math.sin(ball_angle)
ball = pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)

#브릭 설정
brick_width = 75
brick_height = 20
brick_gap = 10
brick_rows = 5
brick_cols = window_width // (brick_width + brick_gap)
bricks = []
brick_colors = []
orange_bricks = []  #주황색 벽돌의 위치를 ​​저장하는 목록

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_gap)
        brick_y = row * (brick_height + brick_gap) + 50
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick)
        if random.uniform(0, 1) < 0.2:
            brick_colors.append(ORANGE)
            orange_bricks.append((brick_x, brick_y))
        else:
            brick_colors.append(BLUE)

#경기 시간 설정
clock = pygame.time.Clock()

#게임 상태 변수 설정
game_started = False
game_over = False
game_won = False

#글꼴 설정
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

#시작 메시지 설정
start_message_text = small_font.render("Press any key to start", True, WHITE)
start_message_rect = start_message_text.get_rect(center=(window_width // 2, window_height // 2))

#게임 오버 메시지 설정
game_over_text = font.render("Game Over", True, WHITE)
game_over_rect = game_over_text.get_rect(center=(window_width // 2, window_height // 2))
stop_continue_text = small_font.render("Press 'S' to stop or 'C' to continue", True, WHITE)
stop_continue_rect = stop_continue_text.get_rect(center=(window_width // 2, window_height // 2 + 50))
congratulations_text = font.render("CONGRATULATIONS!", True, WHITE)
congratulations_rect = congratulations_text.get_rect(center=(window_width // 2, window_height // 2))

#게임 초기화 기능
def reset_game():
    global paddle, ball, bricks, brick_colors, orange_bricks, game_started, game_over, game_won

    paddle.x = paddle_x
    ball.x = ball_x
    ball.y = ball_y
    ball_angle = random.uniform(-math.pi / 4, math.pi / 4)
    ball_dx = ball_speed * math.cos(ball_angle)
    ball_dy = -ball_speed * math.sin(ball_angle)
    bricks = []
    brick_colors = []
    orange_bricks = []
    for row in range(brick_rows):
        for col in range(brick_cols):
            brick_x = col * (brick_width + brick_gap)
            brick_y = row * (brick_height + brick_gap) + 50
            brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
            bricks.append(brick)
            if (brick_x, brick_y) in orange_bricks:
                brick_colors.append(ORANGE)
            else:
                brick_colors.append(BLUE)

    game_started = False
    game_over = False
    game_won = False

#주변 벽돌 부수기 기능
def break_nearby_bricks(x, y):
    for brick in bricks:
        if brick.colliderect(pygame.Rect(x - brick_width, y - brick_height, brick_width * 3, brick_height * 3)):
            if brick_colors[bricks.index(brick)] == BLUE:
                bricks.remove(brick)
                brick_colors.remove(BLUE)
                break

#게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_started:
                game_started = True
            if game_over:
                if event.key == pygame.K_s:
                    running = False  #게임 종료
                elif event.key == pygame.K_c:
                    reset_game()

    if game_started and not game_over and not game_won:
        #패들 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_movement
        if keys[pygame.K_RIGHT] and paddle.right < window_width:
            paddle.x += paddle_movement

        #공을 이동
        ball.x += ball_dx
        ball.y += ball_dy

        #벽과의 충돌 확인
        if ball.left < 0 or ball.right > window_width:
            ball_dx *= -1
        if ball.top < 0:
            ball_dy *= -1

        #패들과의 충돌 확인
        if ball.colliderect(paddle):
            ball_dy *= -1

        #벽돌과의 충돌 확인
        for brick in bricks:
            if ball.colliderect(brick):
                if brick_colors[bricks.index(brick)] == ORANGE:
                    break_nearby_bricks(brick.x, brick.y)
                bricks.remove(brick)
                ball_dy *= -1
                brick_colors.remove(brick_colors[bricks.index(brick)])
                if len(bricks) == 0:
                    game_won = True
                break

        #공이 창밖으로 떨어지는지 확인
        if ball.top > window_height + ball_radius:
            game_over = True

    #창 지우기
    window.fill(BLACK)

    if not game_started:
        #시작 메시지 그리기
        window.blit(start_message_text, start_message_rect)
    elif game_over:
        #메시지 및 옵션을 통해 게임 그리기
        window.blit(game_over_text, game_over_rect)
        window.blit(stop_continue_text, stop_continue_rect)
    elif game_won:
        #축하 메시지 그리기 및 다시 시작 옵션
        window.blit(congratulations_text, congratulations_rect)
        window.blit(stop_continue_text, stop_continue_rect)
    else:
        #패들 그리기
        pygame.draw.rect(window, WHITE, paddle)

        #공을 그립니다
        pygame.draw.circle(window, RED, (ball.x, ball.y), ball_radius)

        #벽돌 그리기
        for brick in bricks:
            pygame.draw.rect(window, brick_colors[bricks.index(brick)], brick)

    #디스플레이 업데이트
    pygame.display.flip()

    #초당 프레임 설정
    clock.tick(60)

#게임 종료
pygame.quit()
