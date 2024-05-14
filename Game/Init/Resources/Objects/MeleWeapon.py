from .Weapon import Weapon
import pygame as pg

class MeleWeapon(Weapon):
    def __init__(self, name, damage, width, height, speed):
        super().__init__(name, damage, width, height, speed)
        self.swing_coordinates = []

    def set_swing_coordinates(self, coordinates):
        self.swing_coordinates = coordinates

    def set_use_coordinates(self, coordinates):
        self.swing_coordinates = coordinates

    def get_hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window, x, y, height, width):
        x_change = self.coordinates[0]
        y_change = self.coordinates[1]
        if self.stage == -1:
            x_change = self.coordinates[0]
            y_change = self.coordinates[1]
        elif self.stage < len(self.swing_coordinates):
            x_change = self.swing_coordinates[self.stage][0]
            y_change = self.swing_coordinates[self.stage][1]
        if self.rotation == 1:
            self.x = x - x_change - self.width
            self.y = y - y_change - self.height // 2
            window.blit(pg.transform.flip(self.image, True, False), (x - x_change - self.width, y - y_change - self.height//2))
        elif self.rotation == -1:
            self.x = x + width + x_change
            self.y = y - y_change - self.height // 2
            window.blit(self.image, (x + width + x_change, y - y_change - self.height//2))