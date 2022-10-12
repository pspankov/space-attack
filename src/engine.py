from typing import Union

import pygame as pg

from .enemy import Enemy
from .config import Config
from .explosion import Explosion
from .laser import Laser
from .meteor import Meteor
from .space_ship import SpaceShip
from .state import State


class Engine:
    def __init__(self, screen: Union[pg.surface.Surface, pg.surface.SurfaceType], state: State, config: Config):
        self.screen = screen
        self.state = state
        self.config = config

        self.enemy_timer = pg.USEREVENT + 1
        self.set_enemy_spawn_time(1500)

        self.meteor_timer = pg.USEREVENT + 2
        self.set_meteor_spawn_time(3000)

        self.space_ship = pg.sprite.GroupSingle(SpaceShip(self.config.p1_ship, self.state))
        self.enemies_group = pg.sprite.Group()
        self.meteors_group = pg.sprite.Group()
        self.lasers_group = pg.sprite.Group()
        self.explosion_group = pg.sprite.Group()

    def reset(self):
        self.state.reset()
        self.space_ship.empty()
        self.space_ship.add(SpaceShip(self.config.p1_ship, self.state))
        self.enemies_group.empty()
        self.meteors_group.empty()
        self.explosion_group.empty()

    def hit(self):
        for laser in self.lasers_group.sprites():
            for enemy_hit in pg.sprite.spritecollide(laser, self.enemies_group, False):
                laser.kill()
                self.explosion_group.add(Explosion(enemy_hit))
                enemy_hit.kill()
                self.state.score += 1
            if len(pg.sprite.spritecollide(laser, self.meteors_group, False)):
                laser.kill()

    def collision(self):
        for enemy in pg.sprite.spritecollide(self.space_ship.sprite, self.enemies_group, True):
            self.explosion_group.add(Explosion(enemy))
            self.explosion_group.add(Explosion(self.space_ship.sprite))
            return True

        for meteor in pg.sprite.spritecollide(self.space_ship.sprite, self.meteors_group, True):
            self.explosion_group.add(Explosion(meteor))
            self.explosion_group.add(Explosion(self.space_ship.sprite))
            return True

        return False

    def handle_state_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:
                    if self.state.game_over:
                        self.reset()
                    elif self.state.running:
                        if self.state.paused:
                            self.state.resume()
                        else:
                            self.state.pause()

    def handle_in_game_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.lasers_group.add(Laser(self.space_ship.sprite.rect.midtop))

            if event.type == self.enemy_timer:
                self.enemies_group.add(Enemy())

            if event.type == self.meteor_timer:
                self.meteors_group.add(Meteor())

    def update(self, events):
        self.handle_state_events(events)

        if self.state.running and not self.state.paused:
            self.handle_in_game_events(events)
            self.space_ship.draw(self.screen)
            self.space_ship.update()

            self.lasers_group.draw(self.screen)
            self.lasers_group.update()

            self.enemies_group.draw(self.screen)
            self.enemies_group.update()

            self.meteors_group.draw(self.screen)
            self.meteors_group.update()

            self.explosion_group.draw(self.screen)
            self.explosion_group.update()

            self.hit()

            if self.collision():
                self.state.lives -= 1
                if self.state.lives < 0:
                    self.state.game_over = True

    def set_enemy_spawn_time(self, time):
        pg.time.set_timer(self.enemy_timer, time)

    def set_meteor_spawn_time(self, time):
        pg.time.set_timer(self.meteor_timer, time)
