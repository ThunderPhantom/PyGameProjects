import time
import random
import pygame
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pong 2')

purple = (128, 0, 128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
colors = [red, green, blue, white]

padx = 295
x_change = 0
y_change = 0
ballx = 320
bally = 240
ballxspeed = 1
ballyspeed = 1
lives = 5

l=[-1,1]

def show_text(msg, x, y, color):
    fontobj = pygame.font.SysFont("freesans", 32)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))

running=True
while running:
    pygame.display.update()
    
    screen.fill(black)
    
    pygame.draw.rect(screen, green, (padx, 470, 75, 10))
    pygame.draw.circle(screen, random.choice(colors), (ballx, bally), 10, 10)
    
    ballx = ballx + ballxspeed
    bally = bally + ballyspeed

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                x_change = -1
            elif event.key == K_RIGHT:
                x_change = 1
        elif event.type == KEYUP:
            if event.key == K_LEFT or K_RIGHT:
                x_change = 0

    padx = padx + x_change
    
    if padx <= 0:
        padx = 0
    
    if padx >= 565:
        padx = 565
    

    if bally == 460 and padx<ballx < padx + 75:
        ballyspeed = -1
    if ballx == 640:
        ballxspeed  = -1
    if bally == 0:
        ballyspeed = 1
    if ballx == 0:
        ballxspeed = 1

    elif bally >= 480:
        lives = lives-1
        ballx = 320
        bally = 240
        ballxspeed = random.choice(l)
        ballyspeed = random.choice(l)

    show_text('You have '+str(lives)+' lives.', 200, 80, red)
    #print(lives)
    if lives==0:
        print('You lose')
        screen.fill(black)
        show_text('You lose!', 200, 80, white)
        pygame.display.update()
        time.sleep(3)
        running  = False

    pygame.display.update()
pygame.quit()

