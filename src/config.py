from configparser import ConfigParser


class ShipConfig:
    def __init__(self, type, color):
        self.type = type
        self.color = color


class Config:
    def __init__(self, path):
        self.config = ConfigParser()
        self.config.read(path)

        self.p1_ship = ShipConfig(self.config.getint('USER', 'p1_ship_type'),
                                  self.config.get('USER', 'p1_ship_color'))

        self.p2_ship = ShipConfig(self.config.getint('USER', 'p2_ship_type'),
                                  self.config.get('USER', 'p2_ship_color'))

    def update(self):
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
