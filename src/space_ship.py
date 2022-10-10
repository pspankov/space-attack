import pygame as pg
import pygame.transform

from .const import SCREEN_WIDTH, SCREEN_HEIGHT


class SpaceShip(pg.sprite.Sprite):
    horizontal_speed = 6
    vertical_speed = 4

    def __init__(self):
        super(SpaceShip, self).__init__()
        self.image = pg.image.load('graphics/png/playerShip1_red.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.7)
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH/2, 600))

    def handle_input(self):
        keys = pg.key.get_pressed()

        if (keys[pg.K_LEFT] or keys[pg.K_a]) and self.rect.left > 0:
            self.rect.x -= self.horizontal_speed
        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.horizontal_speed
        if (keys[pg.K_UP] or keys[pg.K_w]) and self.rect.top > 0:
            self.rect.y -= self.vertical_speed
        if (keys[pg.K_DOWN] or keys[pg.K_s]) and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.vertical_speed

    def update(self):
        self.handle_input()
