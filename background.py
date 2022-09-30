import pygame as pg
from const import MOVING_SPEED


class Background:
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = pg.image.load('graphics/backgrounds/640x480_background.png').convert()
        self.bg_rect = self.bg_image.get_rect()

        self.bg_y1 = 0
        self.bg_x1 = 0

        self.bg_y2 = self.bg_rect.height
        self.bg_x2 = 0

        self.moving_speed = MOVING_SPEED

    def update(self):
        self.bg_y1 += self.moving_speed
        self.bg_y2 += self.moving_speed
        if self.bg_y1 >= self.bg_rect.height:
            self.bg_y1 = -self.bg_rect.height
        if self.bg_y2 >= self.bg_rect.height:
            self.bg_y2 = -self.bg_rect.height

        self.render()

    def render(self):
        self.screen.blit(self.bg_image, (self.bg_x1, self.bg_y1))
        self.screen.blit(self.bg_image, (self.bg_x2, self.bg_y2))
