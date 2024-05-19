# Разработай свою игру в этом файле!
from pygame import *
import time

play = True
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y): 
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class  Player(GameSprite):
    def __init__(self,picture,w,h,x,y, x_speed, y_speed): 
        super().__init__(picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self) :
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

window = display.set_mode((900,800))
display.set_caption('Призрак в лабиринте ')
gost = Player('2.png',50,50,190,200,0,0)
walls = []
walls.append(GameSprite('1.png',120,12,220,270))
walls.append(GameSprite('1.png',12,120,340,210))
walls.append(GameSprite('1.png',120,12,340,200))

while play:
    for i in range(len(walls)):
        walls[i].reset()
    for e in event.get():
        if e.type == QUIT:
            play = False
        if e.type == KEYDOWN:
            if e.key == K_UP:
                gost.y_speed = -1
            elif e.key == K_DOWN:
                gost.y_speed = 1 
            if e.key == K_LEFT:
                gost.x_speed = -1
            elif e.key == K_RIGHT:
                gost.x_speed = 1
        if e.type == KEYUP:
            if e.key == K_UP or e.key == K_DOWN:
                gost.y_speed = 0
            elif e.key == K_LEFT or e.key == K_RIGHT:
                gost.x_speed = 0  
 
    gost.update()
    gost.reset()
    display.update()
display.update()
