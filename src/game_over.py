import pygame as pg

from src.const import SCREEN_WIDTH, SCREEN_HEIGHT


class GameOver(pg.sprite.Sprite):
    def __init__(self):
        super(GameOver, self).__init__()
        self.title_font = pg.font.Font('fonts/kenvector_future_thin.ttf', 35)
        self.title_font.set_italic(True)
        self.color = "white"
        self.subtitle_font = pg.font.Font('fonts/kenvector_future_thin.ttf', 15)

        game_over_txt = self.title_font.render('GAME OVER', True, self.color)
        press_to_continue = self.subtitle_font.render('press <M>', True, self.color)
        self.image = pg.Surface((game_over_txt.get_width(), 300), pg.SRCALPHA)
        self.image.blit(game_over_txt, (0, 0))
        self.image.blit(press_to_continue, (50, 50))
        # self.image = self.font.render('GAME OVER', True, self.color)
        self.rect = self.image.get_rect(midtop=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
