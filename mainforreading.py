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
        fullscreen = fullscreen
        Full_Screen()
        
        window_width = 800
        window_height = 600

        clock = pygame.time.Clock()
        running = True

        # delay before setting the caption
        caption_delay = 1
        time.sleep(caption_delay)

        # display the caption
        pygame.display.set_caption("Brick Break Game")

        # set up crt shader engine
        pygame.display.set_mode((1280,720), pygame.DOUBLEBUF|pygame.OPENGL)
        # pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)        
        from crt_shader import Graphic_engine
        crt_shader = Graphic_engine(screen)

        # border setup
        border_size = 10  # 테두리 크기
        border_color = (4, 111, 255)  # 태두리 색상 (RGB 값)

        # level
        level = Level(crt_shader.render)
        level.title_screen()
        level.menu_state ='title'
    
        # ## set up the player 
        # player_size = 50
        # player_x = (VIRTUAL_RES[0] - player_size) // 2
        # player_y = VIRTUAL_RES[1] - player_size - 10
        # player_speed = 5

        # set up the score as zero
        score = 0

        # Set up game state variables
        game_started =False
        game_over =False
        game_won =False


        # set up the paddle as rectangle
        paddle_width = 100
        paddle_height = 10
        paddle_x = VIRTUAL_RES[0] // 2 - paddle_width // 2
        paddle_y = VIRTUAL_RES[1] - paddle_height - 10
        
        paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
        paddle_movement = 8


        # set up the ball vectors and variables
        ball_radius = 10
        ball_x = window_width //2
        ball_y = window_height //2
        ball_speed = 4
        ball_angle = 0
        #exclude zero degree
        while ball_angle == 0:
            ball_angle = random.uniform(-math.pi / 4, math.pi / 4)  # Random initial angle between -45 and 45 degrees
        #random initail angle between -45 and 45 degrees
        ball_max_speed = 8
        ball_speed_accelaration = 0.00005
        # set up the horizental parameter of ball
        ball_dx = ball_speed * math.cos(ball_angle)
        # set up the vertical parameter of ball
        ball_dy = ball_speed * math.sin(ball_angle)
        # designate the shape of ball by using rect class
        ball = pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)

        # set up the bricks
        brick_width = 75
        brick_height = 20
        brick_gap = 5
        bricks_rows = 5
        brick_cols = window_width // (brick_width + brick_gap)
        bricks = []
        for row in range(bricks_rows):
            for col in range(brick_cols):
                brick_x = col * (brick_width + brick_gap)
                brick_y = row * (brick_height + brick_gap) + 50
                brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
                bricks.append(brick)
        #------------------------------------------------------------

        # Set up fonts # 건: 폰트 추가하면서 들어감1
        font =pygame.font.Font(resource_path('fonts/joystix.ttf'), 36)
        small_font =pygame.font.Font(resource_path('fonts/joystix.ttf'), 24)


        # set up the start message
        start_message_text = small_font.render("Press any key to start", True, black)
        start_message_rect = start_message_text.get_rect(center=(window_width // 2, window_height // 2))


        # Set up game over messages
        game_over_text = font.render("Game Over", True, black)
        game_over_rect = game_over_text.get_rect(center=(window_width //2, window_height //2))
        stop_continue_text = small_font.render("Press 'S' to stop or 'C' to continue", True, black)
        stop_continue_rect = stop_continue_text.get_rect(center=(window_width //2, window_height //2 +50))
        congratulations_text = font.render("CONGRATULATIONS!", True, black)
        congratulations_rect = congratulations_text.get_rect(center=(window_width //2, window_height //2))

    # function to handle ball and paddle collsion # 번역: 공과 패들의 충돌을 처리하는 함수
    def handle_collision(self):
        # global ball_dy
        # reverse the vertical vector of ball
        # 번역: 공의 수직 벡터를 반전시킨다.
        ball_dy = ball_dy * -1

    # function to handle ball movement and speed to give variation to game # 번역: 공의 움직임과 속도를 처리하는 함수
    def handle_ball(self):
        global ball_dx, ball_dy, ball_speed
        # increase ball speed linearly
        if ball_speed < ball_max_speed:
            ball_speed = ball_speed + ball_speed_accelaration
        # adjust ball direction based on speed by using law of pythagoras
        ball_speed_vector = math.sqrt(ball_dx ** 2 + ball_dy ** 2)
        ball_dx = (ball_dx / ball_speed_vector) * ball_speed
        ball_dy = (ball_dy / ball_speed_vector) * ball_speed
        # move the ball by gradual addition
        ball.x = ball.x + ball_dx
        ball.y = ball.y + ball_dy
        # check whether ball collides with the walls
        if ball.left < 0 or ball.right > window_width:
            ball_dx = ball_dx * -1
        if ball.top < 0:
            ball_dy = ball_dy * -1
        # check whether ball collides with the paddle # 번역: 공이 패들과 충돌하는지 확인
        if ball.colliderect(paddle):
            handle_collision() # 번역: 충돌을 처리한다.
        # check the collision with the bricks # 번역: 벽돌과의 충돌을 확인
        for brick in bricks:
            if ball.colliderect(brick):
                bricks.remove(brick)
                handle_collision()
                if len(bricks) == 0:
                    game_won = True
                break
        # check whether the ball falls out of the window # 번역: 공이 창 밖으로 떨어지는지 확인
        if ball.top > window_height + ball_radius:
            game_over = True
            
    #function to reset the game # 번역: 게임을 재설정하는 함수
    def reset_game(self):
        # global paddle, ball, bricks, game_started, game_over, game_won
        paddle.x = paddle_x
        ball.x = ball_x
        ball.y = ball_y
        # ball_angle = random.uniform(-math.pi / 4, math.pi / 4)
        #exclude zero degree    dddssd
        ball_angle = 0
        while ball_angle == 0:
            ball_angle = random.uniform(-math.pi / 4, math.pi / 4)  # Random initial angle between -45 and 45 degrees
        ball_dx =ball_speed *math.cos(ball_angle)
        ball_dy =-ball_speed *math.sin(ball_angle)
        bricks =[]
        for row in range(5):
            for col in range(brick_cols):
                brick_x =col *(brick_width +brick_gap)
                brick_y =row *(brick_height +brick_gap) +50
                brick =pygame.Rect(brick_x, brick_y, brick_width, brick_height)
                bricks.append(brick)

    def run(self):
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    # quit_game()
                if event.type == pygame.KEYDOWN:
                    if not game_started:
                        game_started = True
                    if game_over:
                        if event.key == pygame.K_s:
                            running = False
                        elif event.key == pygame.K_c:
                            if game_over or game_won:
                                reset_game()
                                game_over = False
                                game_won = False
                    if event.key == pygame.K_f:
                        fullscreen = not(fullscreen)
                        Full_Screen()
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # ## Handle player movement # 빨간 블록!
            # keys = pygame.key.get_pressed()
            # if keys[K_LEFT]:
            #     player_x -= player_speed
            # if keys[K_RIGHT]:
            #     player_x += player_speed
            # if keys[K_UP]:
            #     player_y -= player_speed
            # if keys[K_DOWN]:
            #     player_y += player_speed
            # ## Keep the player within the screen bounds
            # player_x = max(0, min(player_x, 800 - player_size))
            # player_y = max(0, min(player_y, 600 - player_size))

            screen.fill('#71ddee')
            # ## Draw the player # 빨간 블록!2!
            # pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))

            # 태두리 그리기
            pygame.draw.rect(screen, border_color, (0, 0, VIRTUAL_RES[0], border_size))  # 상단 태두리
            pygame.draw.rect(screen, border_color, (0, 0, border_size, VIRTUAL_RES[1]))  # 왼쪽 태두리
            pygame.draw.rect(screen, border_color, (0, VIRTUAL_RES[1] - border_size, VIRTUAL_RES[0], border_size))  # 하단 태두리
            pygame.draw.rect(screen, border_color, (VIRTUAL_RES[0] - border_size, 0, border_size, VIRTUAL_RES[1]))  # 오른쪽 태두리


            if game_started and not game_over and not game_won:
                # move the paddle
                keys = pygame.key.get_pressed()
                if keys[K_LEFT] and paddle.left > 0:
                    paddle.x -= paddle_movement
                if keys[K_RIGHT] and paddle.right < window_width:
                    paddle.x += paddle_movement

                # move the ball
                ball.x += ball_dx
                ball.y += ball_dy

                # check for contact with the wall
                # reverse the way of moving
                if ball.left < 0 or ball.right > window_width:
                    ball_dx *= -1
                if ball.top < 0:
                    ball_dy *= -1

                # check for collsion with the paddle
                if ball.colliderect(paddle):
                    ball_dy *= -1
                
                # check for contacts between ball and bricks
                for brick in bricks:
                    if ball.colliderect(brick):
                        bricks.remove(brick)
                        ball_dy *= -1
                        score += 100
                        if len(bricks) == 0:
                            game_won = True
                        break

                # check if ball falls out of the window

                if ball.top > window_height + ball_radius:
                    game_over = True
            
            # clear the window
            screen.fill(white)
            if not game_started:
                # show the start message
                screen.blit(start_message_text, start_message_rect)
            elif game_over:
                # show game over message and options
                screen.blit(game_over_text, game_over_rect)
                screen.blit(stop_continue_text, stop_continue_rect)
            elif game_won:
                # show congratulation message and option to restart
                screen.blit(congratulations_text, congratulations_rect)
                screen.blit(stop_continue_text, stop_continue_rect)
            else:
                # draw the paddle
                pygame.draw.rect(screen, black, paddle)

                # draw the ball
                pygame.draw.circle(screen, red, (ball.x, ball.y), ball_radius)

                # draw the bricks
                for brick in bricks:
                    pygame.draw.rect(screen, blue, brick)

                # draw the score
                score_text = font.render("Score: " + str(score), True, black)
                screen.blit(score_text, (10, 10)) 
                

            # level.run()
            crt_shader.render()
            clock.tick(60)

    def init(self):
        # sprite setup
        __init__(render)


    def Full_Screen(self):
        if fullscreen:
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