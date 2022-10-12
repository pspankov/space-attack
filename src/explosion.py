import pygame as pg


class Explosion(pg.sprite.Sprite):
    default_live = 12
    anim_cycle = 6
    images = []

    def __init__(self, actor: pg.sprite.Sprite):
        pg.sprite.Sprite.__init__(self)
        self.actor = actor
        self.images = [pg.image.load('resources/graphics/png/Lasers/laserRed08.png').convert_alpha(),
                       pg.image.load('resources/graphics/png/Lasers/laserRed09.png').convert_alpha()]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=self.actor.rect.center)
        self.life = self.default_live

    def update(self):
        self.life = self.life - 1
        self.image = self.images[self.life // self.anim_cycle]
        self.rect.center = self.actor.rect.center
        if self.life <= 0:
            self.kill()
