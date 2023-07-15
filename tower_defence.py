import pygame as pg
from enemy import Enemy
from world import World
import constant as c
import json
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
#map  C:/Users/user/AppData/Local/Programs/Python/Python310/Nathan_Python_Games/towerdefence.py/images/assets/sprites/tower_map.png')
map_image = pg.image.load('images/assets/sprites/tower_map.png')
#enemies
enemy_image = pg.image.load('images/assets/sprites/enemies/enemy_1.png').convert_alpha()
#C:/Users/user/AppData/Local/Programs/Python/Python310/Nathan_Python_Games/towerdefence.py/line_map.tmx
with open('images/assets/sprites/enemies/line_map.tmx') as file:
    world_data = json.load(file.read())


#create world
world = World(world_data, map_image)
world.process_data()

#create groups
enemy_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)
#game loop
run = True
while run:

    clock.tick(c.fps)

    screen.fill("grey100")

    #draw level
    World.draw(screen)

    #draw enemy path
    pg.draw.lines(screen, "grey0", False, world.waypoints)

    #update groups
    enemy_group.update()

    #draw groups
    enemy_group.draw(screen)
    
    #event handler
    for event in pg.event.get():
        #quit function
        if event.type == pg.QUIT:
            run = False

    #update display
    pg.display.flip

pg.quit()







