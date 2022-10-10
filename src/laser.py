import pygame as pg


class Laser(pg.sprite.Sprite):
    speed = -11
    attack = 1

    def __init__(self, pos):
        super(Laser, self).__init__()
        self.image = pg.image.load('graphics/png/Lasers/laserRed01.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        sound = pg.mixer.Sound('audio/effects/sfx_laser2.ogg')
        sound.set_volume(0.4)
        sound.play(loops=0)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom <= 0:
            self.kill()
