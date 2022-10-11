import pygame as pg

from src.config import Config
from src.const import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.engine import Engine
from src.music_player import MusicPlayer
from src.screens.background import Background
from src.screens.game_menu import GameMenu
from src.state import State
from src.ui import UI


class Game:
    def __init__(self):

        pg.display.set_caption(GAME_TITLE)

        self.config = Config('config.ini')
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.clock = pg.time.Clock()
        self.state = State()
        self.engine = Engine(self.screen, self.state, self.config)
        self.ui = UI(self.screen, self.state, self.config)
        self.music_player = MusicPlayer(self.state)
        self.background = Background(self.screen)

    def run(self):
        # game loop
        while True:
            events = pg.event.get()

            for event in events:
                if event.type == pg.QUIT:
                    GameMenu.exit()

            self.background.update()
            self.engine.update(events)
            self.ui.update(events)
            self.music_player.update()

            pg.display.update()
            self.clock.tick(FPS)  # ensures that the while loop will not run faster than 60 times/second
