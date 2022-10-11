class State:
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.level = 1
        self.running = False
        self.paused = False
        self._game_over = False

    def reset(self):
        self.lives = 3
        self.score = 0
        self.level = 1
        self.running = False
        self.paused = False
        self._game_over = False

    def start(self):
        self.running = True
        self.paused = False

    def stop(self):
        self.running = False

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    @property
    def game_over(self):
        return self._game_over

    @game_over.setter
    def game_over(self, val: bool):
        self._game_over = val
        if self._game_over:
            self.stop()
