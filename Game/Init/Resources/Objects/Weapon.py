import pygame as pg
class Weapon:
    def __init__(self, name, damage, width, height, speed):
        self.name = name
        self.damage = damage
        self.stage = -1
        self.rotation = -1
        self.width = width
        self.height = height
        self.speed = speed
        self.coordinates = []
        self.x = 0
        self.y = 0
        original_image = pg.image.load('Resources/Sprites/testSword.png')
        self.image = pg.transform.scale(original_image, (width, height))

    def set_coordinates(self, x, y):
        self.coordinates = [x, y]

