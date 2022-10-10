import pygame as pg


class MusicPlayer:
    def __init__(self):
        self.is_playing = False
        self.sounds = {
            'menu': 'audio/start_screen.wav',
            'level_1': 'audio/level_1.wav',
            'level_2': 'audio/level_2.wav',
            'level_3': 'audio/level_3.wav',
            'game_over': 'audio/game_over.wav',
        }
        self.current_sound = None
        self.current_sound_name = ''

    def start(self):
        if not self.is_playing:
            self.current_sound.play(loops=-1)
            self.is_playing = True

    def stop(self):
        if self.is_playing:
            if self.current_sound:
                self.current_sound.stop()
            self.is_playing = False

    def load_sound(self, name):
        if not self.is_playing:
            self.current_sound_name = name
            self.current_sound = pg.mixer.Sound(self.sounds.get(name))
            self.current_sound.set_volume(0.3)

    def play(self, sound):
        if not self.is_playing or self.current_sound_name != sound:
            self.stop()
            self.load_sound(sound)
            self.start()

