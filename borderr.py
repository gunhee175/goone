import pygame

# 화면 크기 설정
width = 800
height = 600
border_size = 10  # 태두리 크기
border_color = (255, 255, 255)  # 태두리 색상 (RGB 값)

# 태두리 크기를 포함한 전체 화면 크기 계산
window_width = width + border_size * 2
window_height = height + border_size * 2

# 화면 생성
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))

# 태두리 그리기
pygame.Rect()
# pygame.draw.rect(screen, border_color, (0, 0, window_width, border_size))  # 상단 태두리
pygame.draw.rect(screen, border_color, (0, 0, border_size, window_height))  # 왼쪽 태두리
pygame.draw.rect(screen, border_color, (0, window_height - border_size, window_width, border_size))  # 하단 태두리
# pygame.draw.rect(screen, border_color, (window_width - border_size, 0, border_size, window_height))  # 오른쪽 태두리

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 로직 및 그리기 작업
    # ...

    pygame.display.flip()

pygame.quit()
