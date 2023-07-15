import pygame as pg
from enemy import Enemy
import constant as c
pg.init()

#clock
clock = pg.time.Clock()

SCREEN_WITDTH = 500
SCREEN_HIGHT = 500
fps = 60

#game window
screen = pg.display.set_mode((c.SCREEN_WITDTH, c.SCREEN_HIGHT))
pg.display.set_caption("tower defence")

#load image
enemy_image = pg.image.load('C:/Users/User/Documents/coding/towerdefence.py/images/assets/Blue/Weapons/turret_01_mk1.png').convert_alpha()

enemy = Enemy()

#game loop
run = True
while run:

    clock.tick(c.fps)
    
    #event handler
    for event in pg.event.get():
        #quit function
        if event.type == pg.QUIT:
            run = False

pg.quit()
        
'C:/Users/user/AppData/Local/Programs/Python/Python310/Nathan_Python Games/defencegame.py/bullet/Bullet.png'






