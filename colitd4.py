import pygame

#둘다 움직임

# 초기화
pygame.init()

# 화면 크기 설정
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# 물체1
obj1_x = 200
obj1_y = 200
obj1_width = 50
obj1_height = 50
obj1_color = (255, 0, 0)
obj1_velocity = 5

# 물체2
obj2_x = 400
obj2_y = 300
obj2_width = 50
obj2_height = 50
obj2_color = (0, 0, 255)
obj2_velocity = 3

# 폰트 설정
font = pygame.font.Font(None, 36)

# 충돌 메시지 표시 함수
def show_collision_message():
    text = font.render("물체1과 물체2가 충돌했습니다.", True, (255, 255, 255))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 물체 이동
    obj1_x += obj1_velocity
    obj2_x += obj2_velocity

    # 충돌 감지
    obj1_rect = pygame.Rect(obj1_x, obj1_y, obj1_width, obj1_height)
    obj2_rect = pygame.Rect(obj2_x, obj2_y, obj2_width, obj2_height)
    if obj1_rect.colliderect(obj2_rect):
        show_collision_message()

    # 화면 지우기
    screen.fill((0, 0, 0))

    # 물체 그리기
    pygame.draw.rect(screen, obj1_color, (obj1_x, obj1_y, obj1_width, obj1_height))
    pygame.draw.rect(screen, obj2_color, (obj2_x, obj2_y, obj2_width, obj2_height))

    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()
