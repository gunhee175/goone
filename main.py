import pygame, sys
from settings import *
from level import Level
from pygame.locals import *

class Game:
    def __init__(self, fullscreen=False):
        # general setup
        pygame.init()
        # # fullscreen setup
        self.fullscreen = fullscreen
        self.Full_Screen()
        
        self.clock = pygame.time.Clock()
        self.running = True

        pygame.display.set_mode((1280,720), pygame.DOUBLEBUF|pygame.OPENGL)
        # pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)        
        from crt_shader import Graphic_engine
        self.crt_shader = Graphic_engine(screen)

        # level
        self.level = Level(self.crt_shader.render)
        self.level.title_screen()
        self.level.menu_state ='title'
    
        ## set up the player
        self.player_size = 50
        self.player_x = (800 - self.player_size) // 2
        self.player_y = 600 - self.player_size - 10
        self.player_speed = 5

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.fullscreen = not(self.fullscreen)
                        self.Full_Screen()

            ## Handle player movement
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.player_x -= self.player_speed
            if keys[K_RIGHT]:
                self.player_x += self.player_speed
            if keys[K_UP]:
                self.player_y -= self.player_speed
            if keys[K_DOWN]:
                self.player_y += self.player_speed

            ## Keep the player within the screen bounds
            self.player_x = max(0, min(self.player_x, 800 - self.player_size))
            self.player_y = max(0, min(self.player_y, 600 - self.player_size))

            screen.fill('#71ddee')
            ## Draw the player
            pygame.draw.rect(screen, (255, 0, 0), (self.player_x, self.player_y, self.player_size, self.player_size))

            self.level.run()
            self.crt_shader.render()
            self.clock.tick(60)

    def Full_Screen(self):
        if self.fullscreen:
            pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL|pygame.FULLSCREEN)
        else:
            pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)

    def quit_game(self):
        pygame.quit()
        sys.exit()

def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    main()