from sys import exit


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
        return self.MenuItem(menu_surf, menu_surf.get_rect(center=pos), action, selected)


class GameMenu:
    def __init__(self, pygame, screen):
        """
        :type pygame: pygame
        :type screen: Union[pygame.surface.Surface, pygame.surface.SurfaceType]
        """
        self.pygame = pygame
        self.screen = screen
        self.is_active = True
        self.game_font = self.pygame.font.Font('fonts/kenvector_future_thin.ttf', 30)
        self.menu_factory = MenuItemFactory(self.game_font, 'White')
        self.menu_items = [
            self.menu_factory.create('1 Player', (400, 50), None, True),
            self.menu_factory.create('2 Players', (400, 100), None),
            self.menu_factory.create('Options', (400, 150), None),
            self.menu_factory.create('Exit', (400, 200), lambda: [pygame.quit(), exit()])
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
        if self.is_active:
            self.handle_events(events)
            self.show()

    def handle_events(self, events):
        for event in events:
            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_DOWN:
                    self.select_item(1)
                if event.key == self.pygame.K_UP:
                    self.select_item(-1)
                if event.key == self.pygame.K_RETURN:
                    self.get_selected().action()

    def show(self):
        # highlight effect of active item
        self.pygame.draw.rect(self.screen, 'Gray', self.get_selected())
        for menu_item in self.menu_items:
            self.screen.blit(menu_item.surf, menu_item.rect)
