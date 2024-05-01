import pygame as pg
class Weapon:
    def __init__(self, name, damage, width, height, speed, duel_wield=False):
        self.name = name
        self.damage = damage
        self.stage = -1
        self.rotation = -1
        self.width = width
        self.height = height
        self.speed = speed
        self.duel_wield = duel_wield
        self.coordinates = []
        self.swing_coordinates = []
        self.x = 0
        self.y = 0

    def set_coordinates(self, x, y):
        self.coordinates = [x, y]

    def set_use_coordinates(self, coordinates):
        self.swing_coordinates = coordinates

    def draw(self, window, x, y, height, width):
        x_change = 0
        y_change = 0
        if self.stage == -1:
            x_change = self.coordinates[0]
            y_change = self.coordinates[1]
        elif self.stage < len(self.swing_coordinates):
            x_change = self.swing_coordinates[self.stage][0]
            y_change = self.swing_coordinates[self.stage][1]
        if self.rotation == 1:
            self.x = x - x_change - self.width
            self.y = y - y_change - self.height // 2
            pg.draw.rect(window, (0, 0, 255), (x - x_change - self.width, y - y_change - self.height//2, self.width, self.height))
        elif self.rotation == -1:
            self.x = x + width + x_change
            self.y = y - y_change - self.height // 2
            pg.draw.rect(window, (0, 0, 255), (x + width + x_change, y - y_change - self.height//2, self.width, self.height))

    def get_hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

