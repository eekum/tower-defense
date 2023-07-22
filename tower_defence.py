import pygame as pg
from enemy import Enemy
from world import World
from turret import Turret
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
#individual turret umage for mouse curser
cursor_turret = pg.image.load('images/assets/sprites/Weapons/turret_1.gif').convert_alpha()
#enemies
enemy_image = pg.image.load('images/assets/sprites/enemies/enemy_1.png').convert_alpha()
#C:/Users/user/AppData/Local/Programs/Python/Python310/Nathan_Python_Games/tower-defence.py/line_map.tmx
#'images/assets/sprites/enemies/line_map.tmx'
with open('C:/Users/user/AppData/Local/Programs/Python/Python310/Nathan_Python_Games/tower-defence.py/line_map.tmx') as file:
    world_data = json.load(file)

def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
    mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
    turret = Turret(cursor_turret, mouse_tile_x, mouse_tile_y)
    turret_group.add(turret)



#create world
world = World(world_data, map_image)
world.process_data()

#create group
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

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
    turret_group.draw(screen)
    
    #event handler
    for event in pg.event.get():
        #quit function
        if event.type == pg.QUIT:
            run = False
        #mouse click
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            #check if mouse is on the game area
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HIGHT:
                create_turret(mouse_pos)
    #update display
    pg.display.flip()

pg.quit()







