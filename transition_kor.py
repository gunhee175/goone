import pygame
import sys, os

# Pygame 초기화
pygame.init()

# 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 게임 창 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("게임 제목")

# 게임 상태
TITLE_SCREEN = 0
MENU_SCREEN = 1
INGAME_SCREEN = 2
GAMEOVER_SCREEN = 3

current_screen = TITLE_SCREEN

# 게임 패키징을 위한 함수
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

def title_screen():
    # 타이틀 화면 표시
    screen.fill(BLACK)
    # title_font = pygame.font.SysFont("joystixmonospaceregular", 60)
    title_font = pygame.font.Font(resource_path('fonts/joystix.ttf'), 60)
    title_text = title_font.render("Game Title", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))
    pygame.display.flip()

def menu_screen():
    # 메뉴 화면 표시
    screen.fill(BLACK)
    menu_font = pygame.font.SysFont("joystixmonospaceregular", 30)
    menu_text = menu_font.render("Press SPACE to Start", True, WHITE)
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, 300))
    pygame.display.flip()

def in_game_screen():
    # 게임 중 화면 표시
    screen.fill(BLACK)
    in_game_font = pygame.font.SysFont("joystixmonospaceregular", 30)
    in_game_text = in_game_font.render("In-Game Screen", True, GREEN)
    screen.blit(in_game_text, (SCREEN_WIDTH // 2 - in_game_text.get_width() // 2, 300))
    pygame.display.flip()

def gameover_screen():
    # 게임 오버 화면 표시
    screen.fill(BLACK)
    gameover_font = pygame.font.SysFont("joystixmonospaceregular", 30)
    gameover_text = gameover_font.render("Game Over", True, RED)
    screen.blit(gameover_text, (SCREEN_WIDTH // 2 - gameover_text.get_width() // 2, 300))
    pygame.display.flip()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if current_screen == TITLE_SCREEN:
                current_screen = MENU_SCREEN
            elif current_screen == MENU_SCREEN and event.key == pygame.K_SPACE:
                current_screen = INGAME_SCREEN
            elif current_screen == INGAME_SCREEN:
                # 게임 로직 추가
                pass
            elif current_screen == GAMEOVER_SCREEN:
                if event.key == pygame.K_SPACE:
                    current_screen = TITLE_SCREEN
    
    # 현재 화면 렌더링
    if current_screen == TITLE_SCREEN:
        title_screen()
    elif current_screen == MENU_SCREEN:
        menu_screen()
    elif current_screen == INGAME_SCREEN:
        in_game_screen()
    elif current_screen == GAMEOVER_SCREEN:
        gameover_screen()

# Pygame 종료
pygame.quit()
sys.exit()
