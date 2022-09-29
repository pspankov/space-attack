import pygame
from sys import exit

from const import WINDOW_NAME
from game_menu import GameMenu


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption(WINDOW_NAME)
    clock = pygame.time.Clock()

    sky_surf = pygame.image.load('graphics/backgrounds/darkPurple.png').convert()

    game_menu = GameMenu(pygame, screen)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(sky_surf, (300, 0))
        game_menu.update(events)
        pygame.display.update()
        clock.tick(60)  # ensures that the while loop will not run faster than 60 times/second


if __name__ == '__main__':
    main()