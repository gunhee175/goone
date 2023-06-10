import pygame

# 초기화
pygame.init()

# 화면 크기 설정
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# 벽 설정
wall_thickness = 10

# 물체1
obj1_x = 200
obj1_y = 200
obj1_width = 50
obj1_height = 50
obj1_color = (255, 0, 0)
obj1_velocity = 5

# 사용자 조종 물체
user_x = 400
user_y = 300
user_width = 50
user_height = 50
user_color = (0, 0, 255)
user_velocity = 3

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 사용자 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        user_x -= user_velocity
    if keys[pygame.K_RIGHT]:
        user_x += user_velocity
    if keys[pygame.K_UP]:
        user_y -= user_velocity
    if keys[pygame.K_DOWN]:
        user_y += user_velocity

    # 벽 밖으로 나가지 않도록 제한
    if obj1_x < wall_thickness:
        obj1_x = wall_thickness
    if obj1_x + obj1_width > width - wall_thickness:
        obj1_x = width - obj1_width - wall_thickness
    if obj1_y < wall_thickness:
        obj1_y = wall_thickness
    if obj1_y + obj1_height > height - wall_thickness:
        obj1_y = height - obj1_height - wall_thickness

    if user_x < wall_thickness:
        user_x = wall_thickness
    if user_x + user_width > width - wall_thickness:
        user_x = width - user_width - wall_thickness
    if user_y < wall_thickness:
        user_y = wall_thickness
    if user_y + user_height > height - wall_thickness:
        user_y = height - user_height - wall_thickness

    # 화면 지우기
    screen.fill((0, 0, 0))

    # 벽 그리기
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, wall_thickness))  # 상단 벽
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, wall_thickness, height))  # 왼쪽 벽
    pygame.draw.rect(screen, (255, 255, 255), (0, height - wall_thickness, width, wall_thickness))  # 하단 벽
    pygame.draw.rect(screen, (255, 255, 255), (width - wall_thickness, 0, wall_thickness, height))  # 오른쪽 벽

    # 물체 그리기
    pygame.draw.rect(screen, obj1_color, (obj1_x, obj1_y, obj1_width, obj1_height))
    pygame.draw.rect(screen, user_color, (user_x, user_y, user_width, user_height))

    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()

