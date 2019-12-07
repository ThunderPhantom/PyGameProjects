import pygame
from pygame.locals import*
pygame.init()
import random
import time
from TicTacToe import tictactoe
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Game Menu')
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
colors = [red, green, blue, white]
def show_text(msg, color, size, x, y):
    fontobj = pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))
def game_menu():
    pygame.draw.rect(screen, red, (0, 60, 300, 60), 10)
    show_text('Tic-Tac-Toe', red, 50, 3, 65)
    pygame.draw.rect(screen, green, (0, 120, 300, 60), 10)
    show_text('Pong Single Player', green, 35, 3, 125)
    pygame.draw.rect(screen, blue, (0, 180, 300, 60), 10)
    show_text('Pong Multiplayer', blue, 40, 3,  185)
    pygame.draw.rect(screen, red, (0, 240, 300,  60),10)
    show_text('Flappy Bird', red, 50, 3, 245)
    pygame.draw.rect(screen, green, (0, 300, 300, 60),10)
    show_text('Snake', green, 50, 3, 305)
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print('You clicked at', event.pos)
            xclick = event.pos [0]
            yclick = event.pos [1]
            if xclick > 0 and xclick < 300 and yclick > 60 and yclick < 120:
                screen.fill(black)
                tictactoe()
            if xclick > 0 and xclick < 300 and yclick > 120 and yclick < 180:
                import Pong1player
            if xclick > 0 and xclick < 300 and yclick > 180 and yclick < 240:
                import Pong2player
            if xclick > 0 and xclick < 300 and yclick > 240 and yclick < 300:
                import FlappyBird
            if xclick > 0 and xclick < 300 and yclick > 300 and yclick < 360:
                import Snake
    show_text('Games', random.choice(colors), 50, 3, 5)
    game_menu()

    
