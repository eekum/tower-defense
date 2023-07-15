import pygame as pg

#pos = possition
class Enemy(pg.sprite.Sprite):
    def __innit__(self, pos, image):   
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_react()
        self.rect.center = pos


