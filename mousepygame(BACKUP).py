#This is a updated version of SpriteHunt.
import pygame
import random
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE=(0, 0, 255)
GREEN=(0, 255, 0)
YELLOW=(255, 255, 0)
BROWN=(160, 82, 45)
ORANGE=(255, 165, 0)
PINK=(255, 192, 203)
PURPLE=(160, 32, 240)
SplotchColors=RED, BLUE, GREEN, YELLOW, BROWN, ORANGE, PINK, PURPLE 
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__() 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
pygame.init()
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group() 
for i in range(10):
    COLORS=random.choice(SplotchColors)
    block = Block(COLORS, 20, 15)
    block.rect.x = random.randrange(SCREEN_WIDTH)
    block.rect.y = random.randrange(SCREEN_HEIGHT)
    block_list.add(block)
    all_sprites_list.add(block)
player = Block(RED, 20, 15)
all_sprites_list.add(player) 
done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
score = 0
level = 1000 
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)  
    for block in blocks_hit_list:
        score += 1
        print( score )
    if len(block_list) == 0:
        level += 1
        for i in range(level * 10):
            COLORS=random.choice(SplotchColors)
            block = Block(COLORS, 20, 15)
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(SCREEN_HEIGHT)
            block_list.add(block)
            all_sprites_list.add(block)
    screen.fill(WHITE)
    all_sprites_list.draw(screen)     
    text = font.render("Score: "+str(score), True, BLACK)
    screen.blit(text, [10, 10])         
    text = font.render("Level: "+str(level), True, BLACK)
    screen.blit(text, [10, 40])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
