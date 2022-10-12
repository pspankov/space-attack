import pygame as pg
from src.state import State

from .config import ShipConfig
from .const import SCREEN_WIDTH, SCREEN_HEIGHT


class SpaceShip(pg.sprite.Sprite):
    horizontal_speed = 6
    vertical_speed = 4

    def __init__(self, ship_config: ShipConfig, game_state: State):
        super(SpaceShip, self).__init__()

        self.ship_config = ship_config
        self.game_state = game_state
        self.last_life_count = -1
        self.space_ship_image = pg.image.load(
            f'resources/graphics/png/playerShip{ship_config.type}_{ship_config.color}.png').convert_alpha()
        self.damage = [
            pg.image.load(f'resources/graphics/png/Damage/playerShip{ship_config.type}_damage3.png').convert_alpha(),
            pg.image.load(f'resources/graphics/png/Damage/playerShip{ship_config.type}_damage2.png').convert_alpha(),
            pg.image.load(f'resources/graphics/png/Damage/playerShip{ship_config.type}_damage1.png').convert_alpha()]
        self.get_image()
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH / 2, 600))

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
        self.get_image()

    def get_image(self):
        if self.game_state.lives != self.last_life_count:
            self.last_life_count = self.game_state.lives
            if self.last_life_count == 3:
                self.image = self.space_ship_image
            else:
                self.image = pg.Surface(self.space_ship_image.get_size(), pg.SRCALPHA)
                self.image.blit(self.space_ship_image, (0, 0))
                self.image.blit(self.damage[self.last_life_count], (0, 0))

            self.image = pg.transform.rotozoom(self.image, 0, 0.7)
