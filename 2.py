import pygame
import random
import math

# 종혁이가 금요일 저녁에 보낸 코드

# Initialize Pygame
pygame.init()

score = 0
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Brick Break Game")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Set up the paddle rectangle
paddle_width = 100
paddle_height = 10
paddle_x = window_width // 2 - paddle_width // 2
paddle_y = window_height - paddle_height - 10
paddle_movement = 5
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# Set up the ball variables
#건:(ball_angle 이 0일 경우에 대한 예외 처리를 추가함)
ball_radius = 10
ball_x = window_width // 2
ball_y = window_height // 2
ball_speed = 4
ball_angle = 0
while ball_angle == 0:
    ball_angle = random.uniform(-math.pi / 4, math.pi / 4)  # Random initial angle between -45 and 45 degrees
ball_dx = ball_speed * math.cos(ball_angle)
ball_dy = -ball_speed * math.sin(ball_angle)
ball = pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)

# Set up the bricks
brick_width = 75
brick_height = 20
brick_gap = 10
brick_rows = 5
brick_cols = window_width // (brick_width + brick_gap)
bricks = []
brick_colors = []
orange_bricks = []  # List to store the positions of orange bricks

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_gap)
        brick_y = row * (brick_height + brick_gap) + 50
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick)
        #아래 코드는 벽돌 색상을 무작위로 할당하는 부분입니다.
        if random.uniform(0, 1) < 0.2:#random.uniform(0, 1) 함수를 사용하여 0과 1 사이에서 무작위로 생성된 숫자가 0.2보다 작으면 
            brick_colors.append(ORANGE)#벽돌 색상을 ORANGE로 설정하고, 
            orange_bricks.append((brick_x, brick_y))# 해당 벽돌의 위치를 orange_bricks 리스트에 추가합니다. 
        else:# 그렇지 않으면 
            brick_colors.append(BLUE)#벽돌 색상을 BLUE로 설정합니다.

# Set up the game clock
clock = pygame.time.Clock()

# Set up game state variables
game_started = False
game_over = False
game_won = False

# Set up fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Set up the start message
start_message_text = small_font.render("Press any key to start", True, WHITE)
start_message_rect = start_message_text.get_rect(center=(window_width // 2, window_height // 2))

# Set up game over messages
game_over_text = font.render("Game Over", True, WHITE)
game_over_rect = game_over_text.get_rect(center=(window_width // 2, window_height // 2))
stop_continue_text = small_font.render("Press 'S' to stop or 'C' to continue", True, WHITE)
stop_continue_rect = stop_continue_text.get_rect(center=(window_width // 2, window_height // 2 + 50))
congratulations_text = font.render("CONGRATULATIONS!", True, WHITE)
congratulations_rect = congratulations_text.get_rect(center=(window_width // 2, window_height // 2))

#난이도 증가
def difficulty():
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width - 15, paddle_height)
    ball_speed + 1.5
    ball = pygame.Rect(ball_x, ball_y, ball_radius * 2 - 40, ball_radius * 2 - 40)

    
# Function to reset the game
def reset_game():
    global paddle, ball, bricks, brick_colors, orange_bricks, game_started, game_over, game_won, ball_dx, ball_dy

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

def break_nearby_bricks(x, y):
    for brick in bricks[:]:  # Use a copy of bricks list to iterate safely
        if brick.colliderect(pygame.Rect(x - brick_width, y - brick_height, brick_width * 3, brick_height * 3)):
            index = bricks.index(brick)
            # if brick_colors[index] == BLUE:
            #     bricks.remove(brick)
            #     brick_colors.pop(index)
            #     break
            
# Set up fonts
score_font = pygame.font.Font(None, 36)

# Game loop
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
                    running = False  # Exit the game
                elif event.key == pygame.K_c:
                    reset_game()

    if game_started and not game_over and not game_won:
        # Move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_movement
        if keys[pygame.K_RIGHT] and paddle.right < window_width:
            paddle.x += paddle_movement

        # Move the ball
        ball.x += ball_dx
        ball.y += ball_dy

        # Check for collisions with the walls
        if ball.left < 0 or ball.right > window_width:
            ball_dx *= -1
        if ball.top < 0:
            ball_dy *= -1

        # Check for collision with the paddle
        if ball.colliderect(paddle):
            ball_dy *= -1

        # Check for collision with the bricks
        for brick in bricks:
            if ball.colliderect(brick):
                if brick_colors[bricks.index(brick)] == ORANGE:
                    break_nearby_bricks(brick.x, brick.y)
                bricks.remove(brick)
                ball_dy *= -1
                score += 100
                if len(bricks) == 0:
                    game_won = True
                break

        #난이도 증가
        if score == 1000:
            difficulty()
        elif score == 2000:
            difficulty()
        elif score == 3000:
            difficulty()

        # Check if ball falls out of the window
        if ball.top > window_height + ball_radius:
            game_over = True

    # Clear the window
    window.fill(BLACK)

    if not game_started:
        # Draw the start message
        window.blit(start_message_text, start_message_rect)
    elif game_over:
        # Draw game over message and options
        window.blit(game_over_text, game_over_rect)
        window.blit(stop_continue_text, stop_continue_rect)
    elif game_won:
        # Draw congratulations message and option to restart
        window.blit(congratulations_text, congratulations_rect)
        window.blit(stop_continue_text, stop_continue_rect)
    else:
        # Draw the paddle
        pygame.draw.rect(window, WHITE, paddle)

        # Draw the ball
        pygame.draw.circle(window, RED, (ball.x, ball.y), ball_radius)

        # Draw the bricks
        for brick in bricks:
            pygame.draw.rect(window, brick_colors[bricks.index(brick)], brick)

        # Draw the score
        score_text = score_font.render("Score: " + str(score), True, WHITE)
        window.blit(score_text, (10, 10))
        
    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)

# Quit the game
pygame.quit()