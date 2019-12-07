
import pygame
import random
from pygame.locals import*
pygame.init()
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
darkgreen = (20, 62, 15)
brown = (149, 20, 0)
yellow = (255, 255, 0)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('snowfall')
circlex = random.randint(1, 639)
circley = 240
xchange = 0#random.randint(1, 639)
ychange = 1
randomcoords = []
colors = [red, green, blue, white]
for i in range(0, 50, 1):
    x=random.randint(0, 640)
    y = random.randint(0, 480)
    randomcoords.append([x, y])
pointlist = [(220, 430), (420, 430), (320, 200)]
def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
while True:

    pygame.display.update()
    screen.fill(black)
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
            exit()
    for s in range(0, 50, 1):
        randomcoords[s][1]=randomcoords[s][1]+1
        pygame.draw.circle(screen, random.choice(colors), (randomcoords[s][0], randomcoords[s][1]),5,5)
    y=randomcoords[s][1]
    
    if y >= 200:
            randomcoords = []
    for i in range(0, 50, 1):
        x=random.randint(0, 640)
        y = random.randint(0, 480)
        randomcoords.append([x, y])
        pygame.draw.line(screen, brown, (320, 480), (320, 430),15)
        pygame.draw.polygon(screen, darkgreen, pointlist)
        show_text('Merry Christmas',100, 50, red, 60)

