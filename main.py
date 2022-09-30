import pygame
from sys import exit

from background import Background
from const import WINDOW_NAME, SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from game_menu import GameMenu
from space_ship import SpaceShip


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_NAME)
    clock = pygame.time.Clock()

    background = Background(screen)
    game_menu = GameMenu(pygame, screen)
    game_menu.show()

    music_is_playing = False
    music = pygame.mixer.Sound('audio/level_1.wav')
    music.set_volume(0.3)

    space_ship = SpaceShip()
    space_ship = pygame.sprite.GroupSingle(space_ship)

    # game loop
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if not game_menu.is_active:
                        game_menu.show()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        background.update()

        if game_menu.is_active:
            game_menu.update(events)
            music_is_playing = False
            music.stop()
        else:
            # gameplay mode
            space_ship.draw(screen)
            space_ship.update()
            if not music_is_playing:
                music_is_playing = True
                music.play(loops=-1)

        pygame.display.update()
        clock.tick(FPS)  # ensures that the while loop will not run faster than 60 times/second


if __name__ == '__main__':
    main()
