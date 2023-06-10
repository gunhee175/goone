import pygame
import time

pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 폰트 설정
font_size = 40
font = pygame.font.Font(None, font_size)

# 텍스트 내용 및 위치 설정
text_content = "Blinking Text"
text_x = screen_width // 2 - font_size * len(text_content) // 2
text_y = screen_height // 2 - font_size // 2

# 깜빡이는 텍스트 표시 여부 설정
show_text = True
blink_interval = 0.5  # 깜빡이는 간격(초)
blink_step = 1

# 게임 루프
running = True
last_blink_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 현재 시간과 마지막 깜빡이는 시간 비교
    current_time = time.time()
    if current_time - last_blink_time >= blink_interval:
        show_text = not show_text
        last_blink_time = current_time

    screen.fill((255, 255, 255))  # 화면을 흰색으로 지움

    if show_text:
        # 텍스트를 화면에 표시
        text_surface = font.render(text_content, True, (255, 0, 0))
        screen.blit(text_surface, (text_x, text_y))

    pygame.display.flip()

pygame.quit()
