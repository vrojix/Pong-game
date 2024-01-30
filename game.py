import pygame,sys 
import random
score = 0
right_score = 0
pygame.time.wait(100)

def restart():
    pygame.time.wait(200)
    moving_rect.update(((screen_w//2)-25),(screen_h//2-25),50,50)
    paddle_1.update(0,starting_height,paddle_width,paddle_height)
    right_paddle.update((screen_w-rpaddle_width),starting_point,paddle_width,paddle_height)




def bounce():
    global x_speed, y_speed,score,right_score
    moving_rect.x+= x_speed
    moving_rect.y+= y_speed

    pygame.draw.rect(screen,(191, 64, 191),moving_rect)
    pygame.draw.rect(screen,(255,255,255),paddle_1)
    pygame.draw.rect(screen,(255,0,0),middle)
    pygame.draw.rect(screen,(255,0,0),right_paddle)
    

    #collision with border

    if moving_rect.right >= screen_w:
        right_score = right_score + 1
        if right_score>=10:
            print("Player 2 Wins")
            pygame.quit()
            quit()
        print(right_score,":Player 2 Side Score")
        x_speed*= -1
        restart()

    if moving_rect.x <= 0:
        score = score + 1
        if score >= 10:
            print("Player 1 Wins")#
            pygame.quit()
            quit()
        print(score,":Left Side Score")
        x_speed*= -1
        restart()

    if moving_rect.bottom >=screen_h or moving_rect.y<= 0:
        y_speed*=-1

    #collision with paddle
    tollerance = 10
    if moving_rect.colliderect(paddle_1):
        if abs(paddle_1.right - moving_rect.left)< tollerance and x_speed <0: 
            x_speed*=-1
        if abs(paddle_1.top - moving_rect.bottom)< tollerance and x_speed>0:
            y_speed*=-1
        if abs(paddle_1.bottom - moving_rect.top)<tollerance and x_speed<0:
            y_speed*=-1
    
    if moving_rect.colliderect(right_paddle):
        if abs(right_paddle.left - moving_rect.right)< tollerance and x_speed>0:
            x_speed*=-1
        if abs(right_paddle.top - moving_rect.bottom)< tollerance and x_speed<0:
            y_speed*=-1
        if abs(right_paddle.bottom - moving_rect.top)<tollerance and x_speed<0:
            y_speed*=-1
    

pygame.init()
screen_w,screen_h = 800,800
screen = pygame.display.set_mode((screen_w,screen_h))
clock = pygame.time.Clock()

moving_rect = pygame.Rect(((screen_w//2)-25),(screen_h//2-25),50,50)
#x_speed, y_speed = random.randint(4,8), random.randint(3,7)
x_speed, y_speed = 8,6

middle = pygame.Rect(screen_w//2,0,1,screen_h)
paddle_height = 250
paddle_width = 14
starting_height = ((((3*screen_h)//4)-screen_h//4) -(paddle_height//2))
paddle_1 = pygame.Rect(0,starting_height,paddle_width,paddle_height)

rpaddle_height = 250
rpaddle_width = 14

starting_point = ((((3*screen_h)//4)-screen_h//4) -(rpaddle_height//2))
right_paddle = pygame.Rect((screen_w-rpaddle_width),starting_point,paddle_width,paddle_height)

vel = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and (paddle_1.y - vel) >= 0:
        paddle_1.y -= vel
    if (keys[pygame.K_s]) and ((paddle_1.y+paddle_height) + vel) <= screen_h:
        paddle_1.y += vel
    if keys[pygame.K_DOWN] and ((right_paddle.y+rpaddle_height) + vel) <= screen_h:
        right_paddle.y+=vel
    if keys[pygame.K_UP] and (right_paddle.y - vel) >= 0:
        right_paddle.y-=vel
    if keys[pygame.K_ESCAPE]:
        pygame.event.wait()

    screen.fill((30, 30, 30))
    bounce()
    pygame.display.flip()
    clock.tick(60)
