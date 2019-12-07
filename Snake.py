import pygame
import time
import random
from pygame.locals import*
pygame.init()
red = (255, 0, 0)
green = (0, 255,  0)
blue = (0, 0,  255)
white = (255,  255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Snake')
snakex = 320
snakey = 240
snakeyspeed = 0
snakexspeed = 0
applex = 320
appley = 240
snakewidth = 20
snakeheight = 20
snakelength = 1
snakelist = []
snakehead = []
mass = 0
game_over = 0
def show_text(msg, color, size, x, y):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
while True:
        pygame.display.update()
        #pygame.draw.rect(screen, green,[snakex, snakey, snakewidth, snakeheight])
        
                           
        snakey = snakey + snakeyspeed
        snakex = snakex + snakexspeed
        for event in pygame.event.get():
               if event.type == KEYDOWN:
                        if event.key == K_UP:
                                snakeyspeed = -1
                        elif event.key == K_DOWN:
                                snakeyspeed = 1
                        elif event.key == K_LEFT:
                                snakexspeed = -1
                        elif event.key == K_RIGHT:
                                snakexspeed = 1
               elif event.type == KEYUP:
                        snakeyspeed = 0
                        snakexspeed = 0
        
        
        #print(snakex,snakey, applex, appley)
        if appley-10<=snakey <= appley+10 and  applex-10<snakex <= applex+10:
                print('collision')
                applex = random.randint(1, 639)
                appley = random.randint(1, 479)
                snakelength = snakelength + 10
                mass = mass + 10
                text = 'Game Over! Your final mass was'+ str(mass)
        snakehead = []
        snakehead.append(snakex)
        snakehead.append(snakey)
        snakelist.append(snakehead)
        screen.fill(black)
        pygame.draw.circle(screen, red, (applex, appley), 10, 10)
        #print(snakelist)
        for xy in snakelist:
                pygame.draw.rect(screen, green,[xy[0], xy[1], 20, 20])
        if len(snakelist)>snakelength:  
                del snakelist[0]
        if snakex >= 640 or  snakex <= 0 or snakey <= 0 or snakey >= 480:
                game_over = 1
                show_text(text, red, 20, 100, 1)
       
        
        if game_over == 1:
                screen.fill(black)
                show_text(text, red, 30, 100, 1)
                

        
                
        
                
                
        
        
                                
