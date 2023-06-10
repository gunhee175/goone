import pygame, sys
import time
import math
import random
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
        
        self.window_width = 800
        self.window_height = 600

        self.clock = pygame.time.Clock()
        self.running = True

        # delay before setting the caption
        self.caption_delay = 1
        time.sleep(self.caption_delay)

        # display the caption
        pygame.display.set_caption("Brick Break Game")

        # set up crt shader engine
        pygame.display.set_mode((1280,720), pygame.DOUBLEBUF|pygame.OPENGL)
        # pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)        
        from crt_shader import Graphic_engine
        self.crt_shader = Graphic_engine(screen)

        # border setup
        self.border_size = 10  # 테두리 크기
        self.border_color = (4, 111, 255)  # 태두리 색상 (RGB 값)

        # level
        self.level = Level(self.crt_shader.render)
        self.level.title_screen()
        self.level.menu_state ='title'
    
        # ## set up the player 
        # self.player_size = 50
        # self.player_x = (VIRTUAL_RES[0] - self.player_size) // 2
        # self.player_y = VIRTUAL_RES[1] - self.player_size - 10
        # self.player_speed = 5

        # set up the score as zero
        self.score = 0

        # Set up game state variables
        self.game_started =False
        self.game_over =False
        self.game_won =False


        # set up the paddle as rectangle
        self.paddle_width = 100
        self.paddle_height = 10
        self.paddle_x = VIRTUAL_RES[0] // 2 - self.paddle_width // 2
        self.paddle_y = VIRTUAL_RES[1] - self.paddle_height - 10
        
        self.paddle = pygame.Rect(self.paddle_x, self.paddle_y, self.paddle_width, self.paddle_height)
        self.paddle_movement = 8


        # set up the ball vectors and variables
        self.ball_radius = 50
        self.ball_x = self.window_width //2
        self.ball_y = self.window_height //2
        self.ball_speed = 4
        self.ball_angle = 0
        #exclude zero degree
        while self.ball_angle == 0:
            self.ball_angle = random.uniform(-math.pi / 4, math.pi / 4)  # Random initial angle between -45 and 45 degrees
        #random initail angle between -45 and 45 degrees
        self.ball_max_speed = 8
        self.ball_speed_accelaration = 0.00005
        # set up the horizental parameter of ball
        self.ball_dx = self.ball_speed * math.cos(self.ball_angle)
        # set up the vertical parameter of ball
        self.ball_dy = self.ball_speed * math.sin(self.ball_angle)
        # designate the shape of ball by using rect class
        self.ball = pygame.Rect(self.ball_x, self.ball_y, self.ball_radius * 2, self.ball_radius * 2)

        # set up the bricks
        self.brick_width = 75
        self.brick_height = 20
        self.brick_gap = 5
        self.bricks_rows = 5
        self.brick_cols = self.window_width // (self.brick_width + self.brick_gap)
        self.bricks = []
        for row in range(self.bricks_rows):
            for col in range(self.brick_cols):
                brick_x = col * (self.brick_width + self.brick_gap)
                brick_y = row * (self.brick_height + self.brick_gap) + 50
                brick = pygame.Rect(brick_x, brick_y, self.brick_width, self.brick_height)
                self.bricks.append(brick)
        #------------------------------------------------------------

        # Set up fonts # 건: 폰트 추가하면서 들어감1
        self.font =pygame.font.Font(resource_path('fonts/joystix.ttf'), 36)
        self.small_font =pygame.font.Font(resource_path('fonts/joystix.ttf'), 24)

        # start message
        self.start_message_text = self.small_font.render("Press any key to start", True, black)
        self.start_message_rect = self.start_message_text.get_rect(center=(self.window_width // 2, self.window_height // 2))

        # game over messages
        self.game_over_text = self.font.render("Game Over", True, black)
        self.game_over_rect = self.game_over_text.get_rect(center=(self.window_width //2, self.window_height //2))
        self.stop_continue_text = self.small_font.render("Press 'S' to stop or 'C' to continue", True, black)
        self.stop_continue_rect = self.stop_continue_text.get_rect(center=(self.window_width //2, self.window_height //2 +50))
        self.congratulations_text = self.font.render("CONGRATULATIONS!", True, black)
        self.congratulations_rect = self.congratulations_text.get_rect(center=(self.window_width //2, self.window_height //2))

    # function to handle ball and paddle collsion # 번역: 공과 패들의 충돌을 처리하는 함수
    def handle_collision(self):
        # reverse the vertical vector of ball 번역: 공의 수직 벡터를 반전시킨다.
        self.ball_dy = self.ball_dy * -1

    #  공의 움직임과 속도를 처리하는 함수
    def handle_ball(self):
        global ball_dx, ball_dy, ball_speed
        # increase ball speed linearly : 
        # 공의 속도를 선형적으로 증가시킨다.
        if ball_speed < self.ball_max_speed:
            ball_speed = ball_speed + self.ball_speed_accelaration
        # adjust ball direction based on speed by using law of pythagoras
        # 피타고라스의 정리를 이용하여 공의 방향을 조정한다.
        ball_speed_vector = math.sqrt(ball_dx ** 2 + ball_dy ** 2)
        ball_dx = (ball_dx / ball_speed_vector) * ball_speed
        ball_dy = (ball_dy / ball_speed_vector) * ball_speed
        # move the ball by gradual addition: 
        # 점진적으로 공을 이동시킨다.
        self.ball.x = self.ball.x + ball_dx
        self.ball.y = self.ball.y + ball_dy
        # check whether ball collides with the walls: 
        # 공이 벽과 충돌하는지 확인
        if self.ball.left < 0 or self.ball.right > self.window_width:
            ball_dx = ball_dx * -1
        if self.ball.top < 0:
            ball_dy = ball_dy * -1
        # check whether ball collides with the paddle  
        # 공이 패들과 충돌하는지 확인
        if self.ball.colliderect(self.paddle):
            self.handle_collision() # 번역: 충돌을 처리한다.
        # check the collision with the bricks 
        # 벽돌과의 충돌을 확인
        for brick in self.bricks:
            if self.ball.colliderect(brick):
                self.bricks.remove(brick)
                self.handle_collision()
                if len(self.bricks) == 0:
                    self.game_won = True
                break
        # check whether the ball falls out of the window # 번역: 
        # 공이 창 밖으로 떨어지는지 확인
        if self.ball.top > self.window_height + self.ball_radius:
            self.game_over = True           
    #function to reset the game
    # 게임을 재설정하는 함수
    def reset_game(self):
        self.paddle.x = self.paddle_x
        self.ball.x = self.ball_x
        self.ball.y = self.ball_y
        #exclude zero degree
        self.ball_angle = 0
        while self.ball_angle == 0:
            self.ball_angle = random.uniform(-math.pi / 4, math.pi / 4)  # Random initial angle between -45 and 45 degrees
        self.ball_dx =self.ball_speed *math.cos(self.ball_angle)
        self.ball_dy =-self.ball_speed *math.sin(self.ball_angle)
        self.bricks =[]
        for row in range(5):
            for col in range(self.brick_cols):
                self.brick_x =col *(self.brick_width +self.brick_gap)
                self.brick_y =row *(self.brick_height +self.brick_gap) +50
                brick =pygame.Rect(self.brick_x, self.brick_y, self.brick_width, self.brick_height)
                self.bricks.append(brick)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    # self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if not self.game_started:
                        self.game_started = True
                    if self.game_over:
                        if event.key == pygame.K_s:
                            self.running = False
                        elif event.key == pygame.K_c:
                            if self.game_over or self.game_won:
                                self.reset_game()
                                self.game_over = False
                                self.game_won = False
                    if event.key == pygame.K_f:
                        self.fullscreen = not(self.fullscreen)
                        self.Full_Screen()
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # ## Handle player movement # 빨간 블록!
            # keys = pygame.key.get_pressed()
            # if keys[K_LEFT]:
            #     self.player_x -= self.player_speed
            # if keys[K_RIGHT]:
            #     self.player_x += self.player_speed
            # if keys[K_UP]:
            #     self.player_y -= self.player_speed
            # if keys[K_DOWN]:
            #     self.player_y += self.player_speed
            # ## Keep the player within the screen bounds
            # self.player_x = max(0, min(self.player_x, 800 - self.player_size))
            # self.player_y = max(0, min(self.player_y, 600 - self.player_size))

            screen.fill('#71ddee')
            # ## Draw the player # 빨간 블록!2!
            # pygame.draw.rect(screen, (255, 0, 0), (self.player_x, self.player_y, self.player_size, self.player_size))



            if self.game_started and not self.game_over and not self.game_won:
                # move the paddle
                keys = pygame.key.get_pressed()
                if keys[K_LEFT] and self.paddle.left > 0:
                    self.paddle.x -= self.paddle_movement
                if keys[K_RIGHT] and self.paddle.right < self.window_width:
                    self.paddle.x += self.paddle_movement

                # move the ball
                self.ball.x += self.ball_dx
                self.ball.y += self.ball_dy

                # check for contact with the wall
                # reverse the way of moving
                if self.ball.left < 0 or self.ball.right > self.window_width:
                    self.ball_dx *= -1
                if self.ball.top < 0:
                    self.ball_dy *= -1

                # check for collsion with the paddle
                if self.ball.colliderect(self.paddle):
                    self.ball_dy *= -1
                
                # check for contacts between ball and bricks
                for brick in self.bricks:
                    if self.ball.colliderect(brick):
                        self.bricks.remove(brick)
                        self.ball_dy *= -1
                        self.score += 100
                        if len(self.bricks) == 0:
                            self.game_won = True
                        break

                # check if ball falls out of the window

                if self.ball.top > self.window_height + self.ball_radius:
                    self.game_over = True
            
            # clear the window
            screen.fill(white)
            if not self.game_started:
                # show the start message
                screen.blit(self.start_message_text, self.start_message_rect)
            elif self.game_over:
                # show game over message and options
                screen.blit(self.game_over_text, self.game_over_rect)
                screen.blit(self.stop_continue_text, self.stop_continue_rect)
            elif self.game_won:
                # show congratulation message and option to restart
                screen.blit(self.congratulations_text, self.congratulations_rect)
                screen.blit(self.stop_continue_text, self.stop_continue_rect)
            else:
                # draw the paddle
                pygame.draw.rect(screen, black, self.paddle)# f

                # draw the ball
                pygame.draw.circle(screen, red, (self.ball.x, self.ball.y), self.ball_radius)

                # draw the bricks
                for brick in self.bricks:
                    pygame.draw.rect(screen, blue, brick)

                # draw the score
                score_text = self.font.render("Score: " + str(self.score), True, black)
                score_text_blink = self.font.render("Score: " + str(self.score), True, black)
                screen.blit(score_text, (10, 10)) 
            
            # 태두리 그리기
            pygame.draw.rect(screen, self.border_color, (0, 0, VIRTUAL_RES[0], self.border_size))  # 상단 태두리
            pygame.draw.rect(screen, self.border_color, (0, 0, self.border_size, VIRTUAL_RES[1]))  # 왼쪽 태두리
            pygame.draw.rect(screen, self.border_color, (0, VIRTUAL_RES[1] - self.border_size, VIRTUAL_RES[0], self.border_size))  # 하단 태두리
            pygame.draw.rect(screen, self.border_color, (VIRTUAL_RES[0] - self.border_size, 0, self.border_size, VIRTUAL_RES[1]))  # 오른쪽 태두리
    
            # self.level.run()
            self.crt_shader.render()
            self.clock.tick(60)

    def init(self):
        # sprite setup
        self.__init__(self.render)


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