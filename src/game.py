import pygame as pg

from .enemy import Enemy
from .laser import Laser
from .meteor import Meteor
from .space_ship import SpaceShip


class Game:
    def __init__(self, screen):
        """
        :type screen: Union[pygame.surface.Surface, pygame.surface.SurfaceType]
        """
        self.screen = screen
        self.level = 1
        self.running = False
        self.game_over = False

        self.enemy_timer = pg.USEREVENT + 1
        self.set_enemy_spawn_time(1500)

        self.meteor_timer = pg.USEREVENT + 2
        self.set_meteor_spawn_time(3000)

        space_ship = SpaceShip()
        self.space_ship = pg.sprite.GroupSingle(space_ship)
        self.enemies_group = pg.sprite.Group()
        self.meteors_group = pg.sprite.Group()
        self.lasers_group = pg.sprite.Group()

    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def collision(self):
        if pg.sprite.spritecollide(self.space_ship.sprite, self.enemies_group, False):
            self.enemies_group.empty()
            return True

        if pg.sprite.spritecollide(self.space_ship.sprite, self.meteors_group, False):
            self.meteors_group.empty()
            return True

        return False

    def hit(self):
        for laser in self.lasers_group.sprites():
            if len(pg.sprite.spritecollide(laser, self.enemies_group, True)):
                laser.kill()
            if len(pg.sprite.spritecollide(laser, self.meteors_group, False)):
                laser.kill()

    def handle_input(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.lasers_group.add(Laser(self.space_ship.sprite.rect.midtop))

            if event.type == self.enemy_timer:
                self.enemies_group.add(Enemy())

            if event.type == self.meteor_timer:
                self.meteors_group.add(Meteor())

    def update(self, events):
        if self.running:
            self.handle_input(events)

            self.space_ship.draw(self.screen)
            self.space_ship.update()

            self.lasers_group.draw(self.screen)
            self.lasers_group.update()

            self.enemies_group.draw(self.screen)
            self.enemies_group.update()

            self.meteors_group.draw(self.screen)
            self.meteors_group.update()

            self.hit()

            if self.collision():
                self.running = False
                self.game_over = True

    def set_enemy_spawn_time(self, time):
        pg.time.set_timer(self.enemy_timer, time)

    def set_meteor_spawn_time(self, time):
        pg.time.set_timer(self.meteor_timer, time)
