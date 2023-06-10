import pygame
import sys

# pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 물체 크기 및 초기 위치 설정
object1_width = 50
object1_height = 50
object1_x = screen_width // 2 - object1_width // 2
object1_y = screen_height // 2 - object1_height // 2
object1_speed = 5

object2_width = 50
object2_height = 50
object2_x = 100
object2_y = 100
object2_speed = 3

# 게임 루프 종료 플래그
game_over = False

font = pygame.font.Font(None, 36)  # 폰트 설정
collision_text = font.render("Collision!", True, (255, 255, 255))  # 텍스트 렌더링
screen.blit(collision_text, (screen_width // 2 - collision_text.get_width() // 2, 10))  # 화면에 텍스트 그리기

while not game_over:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # object1 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and object1_x > 0:
        object1_x -= object1_speed
    if keys[pygame.K_RIGHT] and object1_x < screen_width - object1_width:
        object1_x += object1_speed
    if keys[pygame.K_UP] and object1_y > 0:
        object1_y -= object1_speed
    if keys[pygame.K_DOWN] and object1_y < screen_height - object1_height:
        object1_y += object1_speed

    # object2 이동
    object2_x += object2_speed
    if object2_x < 0 or object2_x > screen_width - object2_width:
        object2_speed *= -1

    # 충돌 검사
    object1_rect = pygame.Rect(object1_x, object1_y, object1_width, object1_height)
    object2_rect = pygame.Rect(object2_x, object2_y, object2_width, object2_height)
    if object1_rect.colliderect(object2_rect):
        # 충돌 시 효과를 줄 수 있습니다. 예를 들어, 화면을 깜빡이거나 메시지를 표시하는 등의 동작을 수행할 수 있습니다.
        print("Collision!")

    if object1_rect.colliderect(object2_rect):
        # 충돌 시 화면 깜빡이기
        pygame.display.set_caption("Collision!")  # 제목에 충돌 메시지 표시
        pygame.font.render("Collision!", True, (255, 255, 255))  # 텍스트 렌더링
        pygame.time.delay(100)  # 100ms 지연
        pygame.display.set_caption("Pygame Window")  # 제목 원래대로 설정

    

    # 화면 그리기
    screen.fill((0, 0, 0))  # 검은색 배경
    pygame.draw.rect(screen, (255, 0, 0), (object1_x, object1_y, object1_width, object1_height))  # object1 그리기
    pygame.draw.rect(screen, (0, 0, 255), (object2_x, object2_y, object2_width, object2_height))  # object2 그리기
    pygame.display.flip()  # 화면 업데이트

