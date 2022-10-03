import pygame as pg
from random import randint

from const import SCREEN_HEIGHT


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pg.image.load('graphics/png/Enemies/enemyBlack1.png').convert_alpha()
        self.image = pg.transform.rotozoom(self.image, 0, 0.7)
        self.rect = self.image.get_rect(midbottom=(randint(0, 460), - randint(50, 150)))

    def update(self):
        self.rect.y += 5
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y = - randint(25, 250)
            self.rect.x = randint(0, 460)
