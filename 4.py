import pygame
import random
import math
import time


#initialize pygame
pygame.init()

#set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# delay before setting the caption
caption_delay = 1
time.sleep(caption_delay)

# display the caption
pygame.display.set_caption("Brick Break Game")

# set up the score as zero
score = 0

# set up the colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

# Set up game state variables
game_started =False
game_over =False
game_won =False


# set up the paddle as rectangle
paddle_width = 100
paddle_height = 10
paddle_x = window_width // 2 - paddle_width // 2
paddle_y = window_height - paddle_height - 10
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

# set up the game clock
clock = pygame.time.Clock()

# function to handle ball and paddle collsion
def handle_collision():
    global ball_dy
    # reverse the vertical vector of ball
    ball_dy = ball_dy * -1

# function to handle ball movement and speed to give variation to game
def handle_ball():
    global ball_dx, ball_dy, ball_speed
    # increase ball speed linearly
    if ball_speed < ball_max_speed:
        ball_speed = ball_speed + ball_speed_accelaration
    # adjust ball direction based on speed by using law of pythagoras
    ball_speed_vector = math.sprt(ball_dx ** 2 + ball_dy ** 2)
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
    # check whether ball collides with the paddle
    if ball.colliderect(paddle):
        handle_collision()
    # check the collision with the bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            handle_collision()
            if len(bricks) == 0:
                game_won = True
            break
    # check whether the ball falls out of the window
    if ball.top > window_height + ball_radius:
        game_over = True

# Set up fonts
font =pygame.font.Font(None, 36)
small_font =pygame.font.Font(None, 24)


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
        
#function to reset the game
def reset_game():
    global paddle, ball, bricks, game_started, game_over, game_won
    paddle.x = paddle_x
    ball.x = ball_x
    ball.y = ball_y
    ball_angle = random.uniform(-math.pi / 4, math.pi / 4)
    #exclude zero degree
    while math.isclose(ball_angle, 0):
        ball_angle = random.uniform(-math.pi / 4, math.pi /4)
    ball_dx =ball_speed *math.cos(ball_angle)
    ball_dy =-ball_speed *math.sin(ball_angle)
    bricks =[]
    for row in range(5):
        for col in range(brick_cols):
            brick_x =col *(brick_width +brick_gap)
            brick_y =row *(brick_height +brick_gap) +50
            brick =pygame.Rect(brick_x, brick_y, brick_width, brick_height)
            bricks.append(brick)

# Game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
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

    if game_started and not game_over and not game_won:
        # move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_movement
        if keys[pygame.K_RIGHT] and paddle.right < window_width:
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
    window.fill(white)
    if not game_started:
        # show the start message
        window.blit(start_message_text, start_message_rect)
    elif game_over:
        # show game over message and options
        window.blit(game_over_text, game_over_rect)
        window.blit(stop_continue_text, stop_continue_rect)
    elif game_won:
        # show congratulation message and option to restart
        window.blit(congratulations_text, congratulations_rect)
        window.blit(stop_continue_text, stop_continue_rect)
    else:
        # draw the paddle
        pygame.draw.rect(window, black, paddle)

        # draw the ball
        pygame.draw.circle(window, red, (ball.x, ball.y), ball_radius)

        # draw the bricks
        for brick in bricks:
            pygame.draw.rect(window, blue, brick)

        # draw the score
        score_text = font.render("Score: " + str(score), True, black)
        window.blit(score_text, (10, 10)) 
        
    
    # update the display
    pygame.display.flip()
    # set the frames per second
    clock.tick(60)

# quit the game
pygame.quit()