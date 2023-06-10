import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Title")

# Game states
TITLE_SCREEN = 0
MENU_SCREEN = 1
INGAME_SCREEN = 2
GAMEOVER_SCREEN = 3

current_screen = TITLE_SCREEN

def title_screen():
    # Display the title screen
    screen.fill(BLACK)
    title_font = pygame.font.SysFont("Arial", 60)
    title_text = title_font.render("Game Title", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))
    pygame.display.flip()

def menu_screen():
    # Display the menu screen
    screen.fill(BLACK)
    menu_font = pygame.font.SysFont("Arial", 30)
    menu_text = menu_font.render("Press SPACE to Start", True, WHITE)
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, 300))
    pygame.display.flip()

def in_game_screen():
    # Display the in-game screen
    screen.fill(BLACK)
    in_game_font = pygame.font.SysFont("Arial", 30)
    in_game_text = in_game_font.render("In-Game Screen", True, GREEN)
    screen.blit(in_game_text, (SCREEN_WIDTH // 2 - in_game_text.get_width() // 2, 300))
    pygame.display.flip()

def gameover_screen():
    # Display the game over screen
    screen.fill(BLACK)
    gameover_font = pygame.font.SysFont("Arial", 30)
    gameover_text = gameover_font.render("Game Over", True, RED)
    screen.blit(gameover_text, (SCREEN_WIDTH // 2 - gameover_text.get_width() // 2, 300))
    pygame.display.flip()

# Game loop
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
                # Add game logic here
                pass
            elif current_screen == GAMEOVER_SCREEN:
                if event.key == pygame.K_SPACE:
                    current_screen = TITLE_SCREEN
    
    # Render the current screen
    if current_screen == TITLE_SCREEN:
        title_screen()
    elif current_screen == MENU_SCREEN:
        menu_screen()
    elif current_screen == INGAME_SCREEN:
        in_game_screen()
    elif current_screen == GAMEOVER_SCREEN:
        gameover_screen()

# Quit Pygame
pygame.quit()
sys.exit()
