import pygame
from pygame.locals import *

pygame.init()

# Set up the window
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shortest Playable Pygame")

# Set up the player
player_size = 50
player_x = (screen_width - player_size) // 2
player_y = screen_height - player_size - 10
player_speed = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_x -= player_speed
    if keys[K_RIGHT]:
        player_x += player_speed
    if keys[K_UP]:
        player_y -= player_speed
    if keys[K_DOWN]:
        player_y += player_speed

    # Keep the player within the screen bounds
    player_x = max(0, min(player_x, screen_width - player_size))
    player_y = max(0, min(player_y, screen_height - player_size))

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

pygame.quit()
