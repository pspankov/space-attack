import pygame
from sys import exit

from background import Background
from const import WINDOW_NAME, SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from game_menu import GameMenu


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_NAME)
clock = pygame.time.Clock()


def main():
    background = Background(pygame, screen)
    game_menu = GameMenu(pygame, screen)

    # game loop
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # screen.blit(bg, (300, 0))
        background.update()
        game_menu.update(events)
        pygame.display.update()
        clock.tick(FPS)  # ensures that the while loop will not run faster than 60 times/second


if __name__ == '__main__':
    main()
