import pygame as pg
from random import randint
from os import listdir

from .const import SCREEN_HEIGHT, SCREEN_WIDTH


class Meteor(pg.sprite.Sprite):
    images = listdir('graphics/png/Meteors')

    def __init__(self, speed=4):
        super(Meteor, self).__init__()

        self.speed = speed
        enemy_image = f'graphics/png/Meteors/{self.images[randint(0, len(self.images) - 1)]}'
        self.image = pg.image.load(enemy_image).convert_alpha()
        self.image = pg.transform.rotozoom(self.image, 0, 0.7)

        self.rect = self.image.get_rect(
            bottomleft=(randint(0, SCREEN_WIDTH-self.image.get_rect().width), - randint(50, 150))
        )
        self.rect = self.image.get_rect(
            bottomleft=(randint(0, SCREEN_WIDTH-self.image.get_rect().width), - randint(50, 150))
        )

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            self.kill()
