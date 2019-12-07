import pygame
from pygame.locals import*
pygame.init()

pygame.display.set_caption('Pong Classes')

class util:
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255,  255, 255)
    black = (0, 0, 0)
    right_width = 10
    right_height = 50
    right_x = 630
    right_y = 200
    right_color = green
    left_width = 10
    left_height = 50
    left_x = 0
    left_y = 1
    left_color = red
    ball_color = blue
    ball_x = 320
    ball_y = 240
    ball_radius = 10
    screen = pygame.display.set_mode((640, 480))
    rightychange = 0
    leftychange = 0
    
class right_paddle:
    def __init__(self, width, height, x, y, color):
        self.width = width
        self.height = height
        self.x= x
        self.y = y
        self.color = color
        

    def draw(self):
        pygame.draw.rect(utility.screen, utility.green, (self.x,self.y, self.width, self.height))

    def move(self):
        if utility.rightychange == 1:
            self.y = self.y -3
        if utility.rightychange == -1:
            self.y = self.y +3
        if self.y <= 0:
            self.y = 0
        if self.y >= 430:
            self.y = 430
class left_paddle:
    def __init__(self, width, height, x, y, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        pygame.draw.rect(utility.screen, utility.red, (self.x,self.y, self.width, self.height))
    def move(self):
        if utility.leftychange == 1:
           self.y = self.y + 3
        if utility.leftychange == -1:
            self.y = self.y -3
        if self.y <= 0:
            self.y = 0
        if self.y >= 430:
            
            self.y = 430
           
            



class ball:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.ballyspeed = 1
        self.ballxspeed = 1

    def draw(self):
        pygame.draw.circle(utility.screen, utility.blue, (self.x, self.y), self.radius)

    def move(self):
        self.x = self.x + self.ballxspeed
        self.y = self.y + self.ballyspeed
        if self.y >= 480:
            self.ballyspeed = -1
        if self.y <= 0:
            self.ballyspeed = 1
        if self.x >= 640:
           self.x = 320
           self.y = 240
        if self.x <= 0:
            self.x = 320
            self.y = 240
            self.ballxspeed = 1
            self.ballyspeed = -1
    def collision(self, leftx, lefty, rightx, righty):
        if self.x == rightx and righty < self.y < righty+50:
            self.ballxspeed = -1
        if self.x == leftx+10 and lefty < self.y < lefty + 50:
            self.ballxspeed = 1
            
utility = util()
rightpaddle = right_paddle(utility.right_width, utility.right_height, utility.right_x, utility.right_y, utility.right_color)
leftpaddle = left_paddle(utility.left_width, utility.left_height, utility.left_x, utility.left_y, utility.left_color)
ball = ball(utility.ball_color, utility.ball_x, utility.ball_y, utility.ball_radius)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYUP:
            #if event.key == K_UP:
            utility.rightychange = 0
            utility.leftychange = 0
        if event.type == KEYDOWN:
            if event.key == K_UP:
                    #print('hi')
                    utility.rightychange = 1
            elif event.key == K_DOWN:
                #print('lo')
                utility.rightychange = -1
            elif event.key == K_w:
                #print('hi')
                utility.leftychange = -1
                
            elif event.key == K_s:
                #print('hi')
                    utility.leftychange = 1
    utility.screen.fill(util.black)
    #print(utility.right_y)
    rightpaddle.draw()
    leftpaddle.draw()
    rightpaddle.move()
    leftpaddle.move()
    ball.draw()
    ball.move()
    ball.collision(leftpaddle.x, leftpaddle.y, rightpaddle.x, rightpaddle.y)
    bally = util.ball_y - ball.ballyspeed
        
        
