from sys import exit

from const import SCREEN_WIDTH, MENU_COLOR, TITLE_COLOR, GAME_TITLE


class MenuItemFactory:
    def __init__(self, font, color):
        self.font = font
        self.color = color

    class MenuItem:
        def __init__(self, surf, rect, action, selected=False):
            self.surf = surf
            self.rect = rect
            self.action = action
            self.selected = selected

    def create(self, title, pos, action, selected=False):
        menu_surf = self.font.render(title, True, self.color)
        return self.MenuItem(menu_surf, menu_surf.get_rect(midbottom=pos), action, selected)


class GameMenu:
    def __init__(self, pygame, screen):
        """
        :type pygame: pygame
        :type screen: Union[pygame.surface.Surface, pygame.surface.SurfaceType]
        """
        self.pygame = pygame
        self.screen = screen
        self.is_active = False
        menu_font = self.pygame.font.Font('fonts/kenvector_future_thin.ttf', 30)
        # game title
        title_font = self.pygame.font.Font('fonts/kenvector_future.ttf', 40)
        self.title = title_font.render(GAME_TITLE, True, TITLE_COLOR)
        self.title_rect = self.title.get_rect(midbottom=(SCREEN_WIDTH/2, 100))

        self.menu_factory = MenuItemFactory(menu_font, MENU_COLOR)
        self.menu_items = [
            self.menu_factory.create('1 Player', (SCREEN_WIDTH/2, 300), lambda: self.close(), True),
            self.menu_factory.create('2 Players', (SCREEN_WIDTH/2, 350), None),
            self.menu_factory.create('Options', (SCREEN_WIDTH/2, 400), None),
            self.menu_factory.create('Exit', (SCREEN_WIDTH/2, 450), lambda: [pygame.quit(), exit()])
        ]
        self.music_is_playing = True
        self.menu_music = pygame.mixer.Sound('audio/start_screen.wav')
        self.menu_music.set_volume(0.3)

    def get_selected(self):
        for menu_item in self.menu_items:
            if menu_item.selected:
                return menu_item

    def select_item(self, direction=1):
        for idx, menu_item in enumerate(self.menu_items):
            if menu_item.selected:
                menu_item.selected = False
                try:
                    next_item = self.menu_items[idx + direction]
                except IndexError:
                    next_item = self.menu_items[0] if direction == 1 else self.menu_items[-1]
                next_item.selected = True
                return next_item

    def update(self, events):
        self.handle_events(events)
        self.draw()

    def handle_events(self, events):
        for event in events:
            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_DOWN:
                    self.select_item(1)
                if event.key == self.pygame.K_UP:
                    self.select_item(-1)
                if event.key == self.pygame.K_RETURN:
                    self.get_selected().action()

    def draw(self):
        self.screen.blit(self.title, self.title_rect)
        # highlight effect of active item
        self.pygame.draw.rect(self.screen, '#6777b8', self.get_selected())
        for menu_item in self.menu_items:
            self.screen.blit(menu_item.surf, menu_item.rect)

    def show(self):
        self.is_active = True
        self.menu_music.play(loops=-1)
        self.music_is_playing = True

    def close(self):
        self.is_active = False
        self.menu_music.stop()
        self.music_is_playing = False
