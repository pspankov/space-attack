from sys import exit

from .const import SCREEN_WIDTH, MENU_COLOR, TITLE_COLOR, GAME_TITLE


class MenuItemFactory:
    def __init__(self, font, color, pos):
        self.font = font
        self.color = color
        self.start_pos = pos
        self.menu_items = []

    class MenuItem:
        def __init__(self, title, surf, rect, action, selected=False):
            self.title = title
            self.surf = surf
            self.rect = rect
            self.action = action
            self.selected = selected

    def create(self, title, action, selected=False, pos=None):
        menu_surf = self.font.render(title, True, self.color)
        pos = pos or self.start_pos
        self.start_pos = (self.start_pos[0], self.start_pos[1] + 50)
        return self.MenuItem(title, menu_surf, menu_surf.get_rect(midbottom=pos), action, selected)


class GameMenu:
    def __init__(self, pygame, screen, one_p_func):
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

        self.menu_factory = MenuItemFactory(menu_font, MENU_COLOR, (SCREEN_WIDTH/2, 300))
        self.menu_items = [
            self.menu_factory.create('Start', lambda: [self.close(), one_p_func()], True),
            # self.menu_factory.create('2 Players', None),
            self.menu_factory.create('Options', None),
            self.menu_factory.create('Exit', lambda: [pygame.quit(), exit()])
        ]

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

    def close(self):
        self.is_active = False
