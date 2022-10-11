from typing import Union

import pygame as pg
from sys import exit

from ..const import SCREEN_WIDTH, MENU_COLOR, TITLE_COLOR, GAME_TITLE, SCORE_FONT, MENU_ITEM_FONT, GAME_TITLE_FONT
from ..state import State


class MenuItemFactory:
    def __init__(self, font, color, pos):
        self.font = font
        self.color = color
        self.start_pos = pos
        self.menu_items = []

    class MenuItem:
        def __init__(self, title, surf, rect, action, selected=False):
            self.title = title
            self.surf = surf
            self.rect = rect
            self.action = action
            self.selected = selected

    def create(self, title, action, selected=False, pos=None):
        menu_surf = self.font.render(title, True, self.color)
        pos = pos or self.start_pos
        self.start_pos = (self.start_pos[0], self.start_pos[1] + 50)
        return self.MenuItem(title, menu_surf, menu_surf.get_rect(midbottom=pos), action, selected)


class GameMenu:
    def __init__(self, screen: Union[pg.surface.Surface, pg.surface.SurfaceType], game_state: State):
        self.screen = screen
        self.game_state = game_state
        self.is_active = True
        # game title
        self.title = GAME_TITLE_FONT.render(GAME_TITLE, True, TITLE_COLOR)
        self.title_rect = self.title.get_rect(midbottom=(SCREEN_WIDTH/2, 100))

        self.update_score()
        self.score_rect = self.score.get_rect(midbottom=(SCREEN_WIDTH/2, 200))

        self.menu_factory = MenuItemFactory(MENU_ITEM_FONT, MENU_COLOR, (SCREEN_WIDTH/2, 300))
        self.start_menu_items = [
            self.menu_factory.create('Start', lambda: self.start(), True),
            # self.menu_factory.create('2 Players', None),
            self.menu_factory.create('Options', None),
            self.menu_factory.create('Exit', lambda: GameMenu.exit())
        ]
        self.menu_factory.start_pos = (SCREEN_WIDTH/2, 300)
        self.pause_menu_items = [
            self.menu_factory.create('Resume', lambda: self.resume(), True),
            self.menu_factory.create('Exit', lambda: GameMenu.exit())
        ]

    def start(self):
        self.close()
        self.game_state.start()

    def resume(self):
        self.close()
        self.game_state.resume()

    @staticmethod
    def exit():
        pg.quit()
        exit()

    def get_active_menu_items(self):
        if self.game_state.running:
            return self.pause_menu_items
        return self.start_menu_items

    def get_selected(self):
        for menu_item in self.get_active_menu_items():
            if menu_item.selected:
                return menu_item

    def select_item(self, direction=1):
        menu_items = self.get_active_menu_items()
        for idx, menu_item in enumerate(menu_items):
            if menu_item.selected:
                menu_item.selected = False
                try:
                    next_item = menu_items[idx + direction]
                except IndexError:
                    next_item = menu_items[0] if direction == 1 else menu_items[-1]
                next_item.selected = True
                return next_item

    def update(self, events):
        if self.is_active:
            self.draw()
            self.handle_events(events)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.select_item(1)
                if event.key == pg.K_UP:
                    self.select_item(-1)
                if event.key == pg.K_RETURN:
                    self.get_selected().action()

    def draw(self):
        self.screen.blit(self.title, self.title_rect)
        if self.game_state.paused:
            self.update_score()
            self.screen.blit(self.score, self.score_rect)
        # highlight effect of active item
        pg.draw.rect(self.screen, '#6777b8', self.get_selected())
        for menu_item in self.get_active_menu_items():
            self.screen.blit(menu_item.surf, menu_item.rect)

    def update_score(self):
        self.score = SCORE_FONT.render(f'Score: {self.game_state.score}', True, TITLE_COLOR)

    def show(self):
        self.is_active = True

    def close(self):
        self.is_active = False
