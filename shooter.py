import pygame
import time
import random
import math
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('shooter')
red = (255, 0, 0)
orange = (255, 100, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
lightblue = (0, 255, 255)
blue = (0, 0, 255)
indigo = (100, 0, 255)
purple = (200, 0, 255)
pink = (255, 0, 150)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (150, 150, 150)

colors = [red, orange, yellow, green, lightblue, blue, indigo, pink]
randomcoords = []
class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(random.choice(colors))
        self.rect=self.image.get_rect()
        
class Player(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(gray)
        self.rect = self.image.get_rect()

    def draw():
        screen.blit(self.rect)
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, startx, starty, endx, endy):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect=self.image.get_rect()
        self.rect.x = startx
        self.rect.y = starty
        diffx = endx - startx
        diffy = endy - starty
        angle = math.atan2(diffy, diffx)
        speed = 5
        self.change_x = math.cos(angle)*speed
        self.change_y = math.sin(angle)*speed
        self.floating_point_x = startx
        self.floating_point_y = starty    
    def update(self):
        self.floating_point_x += self.change_x
        self.floating_point_y += self.change_y
        self.rect.x = int(self.floating_point_x)
        self.rect.y = int(self.floating_point_y)
        
        if self.change_x == 640 or self.change_y == 480 or self.change_x == 0 or self.change_y == 0:
            self.rect.x = 300
            self.rect.y = 240

        #print(rect.x, rect.y)

        
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

for s in range(0, 150, 1):
    block = Block(green)
    block.rect.x = random.randint(0, 640)
    block.rect.y = random.randint(0, 480)
    block_list.add(block)
    all_sprites_list.add(block)

player = Player(red)
player.rect.x = 320
player.rect.y = 240
all_sprites_list.add(player)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos

            
            bullet = Bullet(white, player.rect.x, player.rect.y, x, y)
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            
    
    all_sprites_list.update()
    for bullets in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullets, block_list, True)
        for block in block_hit_list:
            bullet_list.remove(bullets)
            all_sprites_list.remove(bullets)

    screen.fill(black)
    all_sprites_list.draw(screen)
    pygame.display.flip()
