import pygame
from pygame.locals import*
import random
import time
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Tic-Tac-Toe')



def tictactoe():
    t = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}
    squares = {(0, 0):1, (100, 0):2, (200, 0):3,
               (0, 100):4, (100, 100):5, (200, 100):6,
               (0, 200):7, (100, 200):8, (200, 200):9}
    circles = {1:[0, 0, 100, 100], 2:[100, 0, 200, 100], 3:[200, 0, 300, 100]
               , 4: [0, 100, 100, 200], 5:[100, 100,  200, 300], 6:[200, 100, 300, 200],
               7:[0, 200, 100, 300], 8:[100, 200, 300, 200], 9:[200, 200, 300, 300]}
    x = 0
    y = 0
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    colors = [red, green, blue, white]
    xclick = 0
    yclick = 0
    computerchoice = random.randint(1, 9)
    a = False
    b = False
    whatever = 0
    def show_text(msg, color, size, x, y):
        fontobj = pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg, False, color)
        screen.blit(msgobj, (x, y))

    def check():
        computerchoice = random.randint(1, 9)
        while t[computerchoice] == 'O' or t[computerchoice] == 'X':
            computerchoice = random.randint(1, 9)
        return computerchoice

    def win(mark):
        winvar = 0
        
        for s in range (1, 4, 1):
            if t[s] == mark and t[s+3] == mark and t[s+6] == mark:
                winvar = 1
        for s in range(1, 8, 3):
            if t[s] == mark and t[s+1] == mark and t[s+2] == mark:
                winvar = 1
        if t[1] == mark and t[5] == mark and t[9] == mark:
            winvar = 1
        if t[3] == mark and t[5] == mark and t[7] == mark:
                winvar = 1

        if t[1] != '' and t[2] != '' and t[3] != '' and t[4] != '' and t[5] != '' and t[6] != '' and t[7] != '' and t[8] != '' and t[9] != '' and winvar == 0:
            time.sleep(0.5)
            screen.fill(black)
            show_text('Draw!', white, 32, 100, 150)
            pygame.display.update()
            time.sleep(1.5)
            screen.fill(black)
            time.sleep(0.5)
            winvar = 0 
            return True
            
        if mark == 'X' and winvar == 1:
            time.sleep(0.5)
            screen.fill(black)
            show_text('You win!', green, 32, 100, 150)
            pygame.display.update()
            time.sleep(1.5)
            screen.fill(black)
            time.sleep(0.5)
            winvar = 0

            return True
            
        if mark == 'O' and winvar == 1:
            time.sleep(0.5)
            screen.fill(black)
            show_text('You lose!', red, 32, 100, 150)
            pygame.display.update()
            screen.fill(black)
            time.sleep(1.5)
            time.sleep(0.5)
            winvar = 0
            return True

    while True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
              
                xclick = event.pos [0]
                yclick = event.pos [1]
                xclick = xclick - xclick % 100
                yclick = yclick - yclick % 100

                if not ((t[squares[(xclick,yclick)]]) == 'X' or (t[squares[(xclick,yclick)]]) == 'O'):
                    pygame.draw.line(screen, blue, (xclick, yclick),(xclick + 100, yclick + 100), 5)
                    pygame.draw.line(screen, blue, (xclick + 100, yclick), (xclick, yclick + 100), 5)
                    t[squares[(xclick,yclick)]]='X'
                    whatever = 1
                #print(((t[squares[(xclick,yclick)]]) == 'X', (t[squares[(xclick,yclick)]]) == 'O'))
                a = win('X')
                #print('X',a)
                if a == True:
                    break
                    
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and whatever == 1:
                #print ('O')
                computerchoice = check()
                pygame.draw.circle(screen, random.choice(colors), (circles[computerchoice][0] + 50, circles[computerchoice][1] + 50), 50, 5)
                t[computerchoice] = 'O'
                #print (t)        
        if t[computerchoice] == 'X':
            computerchoice = random.randint(1, 9)
        b = win('O')
        #print('O',a)
        if a == True or b == True:            
            break
        for x in range(0, 300, 100):
            for y in range(0, 300, 100):
                pygame.draw.rect(screen, random.choice(colors), (x, y, 100, 100), 10)
        

    print (t)

        
    

    
       
        
    
        
