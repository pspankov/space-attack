import pygame as pg
from sys import exit

from .background import Background
from .const import GAME_TITLE, SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from .game import Game
from .game_menu import GameMenu
from .game_over import GameOver
from .music_player import MusicPlayer


class GameUI:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        self.clock = pg.time.Clock()

        self.music_player = MusicPlayer()
        self.game = Game(self.screen)

        self.background = Background(self.screen)
        self.game_menu = GameMenu(pg, self.screen, self.game.start)
        self.game_menu.show()
        self.game_over = pg.sprite.Group(GameOver())

    def run(self):
        # game loop
        while True:
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_m:
                        if not self.game_menu.is_active:
                            self.game.running = False
                            self.game.game_over = False
                            self.game_menu.show()
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.background.update()

            if self.game.running:
                # gameplay mode
                self.music_player.play('level_1')
                self.game.update(events)
            elif self.game.game_over:
                # game over screen
                self.music_player.play('game_over')
                self.game_over.draw(self.screen)
            elif self.game_menu.is_active:
                self.music_player.play('menu')
                self.game_menu.update(events)

            pg.display.update()
            self.clock.tick(FPS)  # ensures that the while loop will not run faster than 60 times/second
