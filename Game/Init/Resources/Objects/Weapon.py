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
        original_image = pg.image.load('Resources/Sprites/testSword.png')
        self.image = pg.transform.scale(original_image, (width, height))

    def set_coordinates(self, x, y):
        self.coordinates = [x, y]

    def set_use_coordinates(self, coordinates):
        self.swing_coordinates = coordinates

    def get_hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

