from .Weapon import Weapon
import pygame as pg

class MeleWeapon(Weapon):
    def __init__(self, name, damage, width, height, speed, duel_wield=False):
        super().__init__(name, damage, width, height, speed, duel_wield)
        self.swing_coordinates = []

    def set_swing_coordinates(self, coordinates):
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