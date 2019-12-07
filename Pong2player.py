import time
import random
import pygame
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pong')

purple = (128, 0, 128)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
colors = [red, green, blue, white]

leftx = 0
lefty = 215
rightx = 630
righty = 215
leftx_change = 0
lefty_change = 0
rightx_change = 0
righty_change = 0
ballx = 320
bally = 240
ballxspeed = 2
ballyspeed = 2
leftscore = 0
rightscore = 0

def show_text(msg, x, y, color):
    fontobj = pygame.font.SysFont("freesans", 32)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
    
while True:
    pygame.display.update()
    
    screen.fill(black)
    
    pygame.draw.rect(screen, green, (leftx, lefty, 10, 50))
    pygame.draw.rect(screen, red, (rightx, righty, 10, 50))
    pygame.draw.circle(screen, random.choice(colors), (ballx, bally), 10, 10)
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                righty_change = 3
            elif event.key == K_UP:
                righty_change = -3
            elif event.key == K_w:
                lefty_change= -3
            elif event.key == K_s:
                lefty_change = 3
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                lefty_change = 0
            if event.key == K_DOWN or K_UP:
                righty_change = 0

    #  ============Paddle Movement
    
    lefty = lefty + lefty_change
    if lefty < 0:
        lefty=0
    pygame.display.update
    if lefty >= 430:
        lefty = 430
    pygame.display.update()
    righty = righty + righty_change
    if righty < 0:
        righty=0
    pygame.display.update
    if righty >= 430:
        righty = 430
    pygame.display.update()

    # ============Ball Movement
    ballx = ballx + ballxspeed
    bally = bally+ ballyspeed
    #print(ballyspeed)
    if bally >= 480:
        ballyspeed=-2
    if bally <= 0:
        ballyspeed = 2
    #print(ballx, lefty)
    if ballx == rightx and righty < bally < righty+50:
        #if ballx > rightx-10 and bally == righty :
        ballxspeed = -2
    if ballx == leftx and lefty < bally < lefty + 50:
        ballxspeed = 2
    
    if ballx < 0:
        rightscore = rightscore + 1
        ballx = 320
        bally = 240
        ballxspeed = -2
        ballyspeed = 2
        
        
    if ballx > 640:
        leftscore = leftscore + 1
        ballx = 320
        bally = 240
        ballxspeed = 2
        ballyspeed = -2
    show_text('Left side score: '+str(leftscore), 10, 10, white)     
    show_text('Right side score: '+str(rightscore),  350, 10, white)
    if leftscore == 5:
        screen.fill(black)
        show_text('Left side won!', 150, 10, green)
        time.sleep(2)
        screen.fill(black)
        pygame.display.update()
        break
    if rightscore == 5:
        screen.fill(black)
        show_text('Right side won!', 150, 10, red)
        time.sleep(2)
        screen.fill(black)
        pygame.display.update()
        break
        
    pygame.display.update()
    
    
    
