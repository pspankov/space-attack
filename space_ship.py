import pygame as pg

from const import SCREEN_WIDTH, SPACE_SHIP_SPEED, SCREEN_HEIGHT


class SpaceShip(pg.sprite.Sprite):
    def __init__(self):
        super(SpaceShip, self).__init__()
        self.image = pg.image.load('graphics/png/playerShip1_red.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH/2, 600))

    def handle_input(self):
        keys = pg.key.get_pressed()
        if (keys[pg.K_LEFT] or keys[pg.K_a]) and self.rect.left > 0:
            self.rect.x -= SPACE_SHIP_SPEED
        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and self.rect.right < SCREEN_WIDTH:
            self.rect.x += SPACE_SHIP_SPEED
        if (keys[pg.K_UP] or keys[pg.K_w]) and self.rect.top > 0:
            self.rect.y -= SPACE_SHIP_SPEED
        if (keys[pg.K_DOWN] or keys[pg.K_s]) and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += SPACE_SHIP_SPEED

    def update(self):
        self.handle_input()
