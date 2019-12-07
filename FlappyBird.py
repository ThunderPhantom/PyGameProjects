import time
import random
import pygame
pygame.init()
from pygame.locals import*
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Flappy Bird')
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
screencolor = white
birdx = 320
birdy = 240
birdychange = 2
pipex = 640
running=1
r = random.randint(100, 380)
score = 0
def show_text(msg, x, y, color):
    fontobj = pygame.font.SysFont("freesans", 50)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
while running:
    pygame.display.update()
    screen.fill(screencolor)
    show_text('Score:'+str(score), 1, 10, blue)
    pygame.draw.circle(screen, red, (birdx, birdy), 10, 10)
    pygame.draw.rect(screen, green, (pipex, 0, 75, r))
    pygame.draw.rect(screen, green, (pipex, r + 100, 75, 1000))
    pipex = pipex - 4
    if pipex < 0:
        r = random.randint(100, 380)
        pipex = 640
        pipex = pipex - 4
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                birdychange = -3
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                birdychange = 2
    birdy = birdy + birdychange
    if birdy < 0 or birdy > 480:
        screen.fill(white)
        show_text('You Died! Final Score:'+str(score), 1, 200, blue)
        pygame.display.update()
        time.sleep(2)
        birdx = 320
        birdy = 240
        pipex = 640
        score = 0
        running = 1
    if pipex<birdx < pipex+75 and birdy <r:
        screen.fill(white)
        show_text('You Died! Final Score:'+str(score), 1, 200, blue)
        pygame.display.update()
        time.sleep(2)
        birdx = 320
        birdy = 240
        pipex = 640
        score = 0
        running=1
    if pipex<birdx < pipex+75 and birdy >r+100:
        screen.fill(white)
        show_text('You Died! Final Score:'+str(score), 1, 200, blue)
        pygame.display.update()
        time.sleep(2)
        birdx = 320
        birdy = 240
        pipex = 640
        score = 0
        running=1
    if pipex + 76 == birdx:
        score = score + 1

    
    
        
