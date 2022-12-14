from typing import Union

import pygame as pg

from .const import SCORE_FONT, MENU_COLOR, SCREEN_WIDTH, SCORE_COLOR
from .config import Config, ShipConfig
from .screens.game_menu import GameMenu
from .screens.game_over import GameOver
from .state import State


class UI:
    def __init__(self, screen: Union[pg.surface.Surface, pg.surface.SurfaceType], state: State, config: Config):
        self.screen = screen
        self.game_state = state
        self.config = config

        self.game_menu = GameMenu(self.screen, self.game_state)
        self.game_over = pg.sprite.Group(GameOver())
        self.score = pg.sprite.Group(Score(self.game_state))
        self.life_bar = pg.sprite.Group(LifeBar(self.game_state, config.p1_ship))
        self.level = pg.sprite.Group(Level(self.game_state))

    def handle_input(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:
                    if self.game_menu.is_active:
                        self.game_menu.close()
                    else:
                        self.game_menu.show()

    def update(self, events):
        self.handle_input(events)

        if self.game_state.game_over:
            self.game_over.draw(self.screen)
        elif self.game_state.paused or not self.game_state.running:
            self.game_menu.update(events)
        else:
            self.score.draw(self.screen)
            self.score.update()

            self.life_bar.draw(self.screen)
            self.life_bar.update()

            self.level.draw(self.screen)
            self.level.update()


class Score(pg.sprite.Sprite):
    def __init__(self, game_state: State):
        super(Score, self).__init__()
        self.game_state = game_state
        self.last_score = -1
        self.font = SCORE_FONT
        self.update()
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH / 2, self.image.get_height() + 10))

    def update(self):
        if self.game_state.score != self.last_score:
            self.last_score = self.game_state.score
            self.image = self.font.render(f'Score: {self.game_state.score}', True, SCORE_COLOR)


class LifeBar(pg.sprite.Sprite):
    def __init__(self, game_state: State, ship_config: ShipConfig):
        super(LifeBar, self).__init__()

        self.game_state = game_state
        self.ship_config = ship_config
        self.last_life_count = -1
        life_icon = f"resources/graphics/png/UI/playerLife{self.ship_config.type}_{self.ship_config.color}.png"
        self.life_image = pg.image.load(life_icon).convert_alpha()
        self.life_image = pg.transform.rotozoom(self.life_image, 0, 0.7)
        self.life_bar_width = self.life_image.get_width() * self.game_state.lives + self.game_state.lives * 10

        self.update()
        self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH - self.image.get_width(), 10))

    def update(self):
        if self.game_state.lives != self.last_life_count:
            self.last_life_count = self.game_state.lives

            self.image = pg.Surface((self.life_bar_width, self.life_image.get_height()), pg.SRCALPHA)
            # draw each life icon in the bar
            for life in range(self.game_state.lives):
                self.image.blit(self.life_image, (self.life_image.get_width() * life + 10 * life, 0))


class Level(pg.sprite.Sprite):
    def __init__(self, game_state: State):
        super(Level, self).__init__()
        self.game_state = game_state
        self.last_level = -1
        self.font = SCORE_FONT
        self.update()
        self.rect = self.image.get_rect(topleft=(10, 10))

    def update(self):
        if self.game_state.level != self.last_level:
            self.last_level = self.game_state.level
            self.image = self.font.render(f'Level {self.game_state.level}', True, MENU_COLOR)
