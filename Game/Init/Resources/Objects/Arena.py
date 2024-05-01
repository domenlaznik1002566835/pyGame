import pygame as pg
from .Platform import Platform

class Arena:
    def __init__(self, name, width, height, gravity, floor_y):
        self.name = name
        self.width = width
        self.height = height
        self.gravity = gravity
        self.floor_y = floor_y
        self.platforms = []

    def draw(self, window):
        pg.draw.rect(window, (0, 0, 0), (0, 0, self.width, self.height))
        pg.draw.line(window, (255, 255, 255), (0, self.height - self.floor_y), (self.width, self.height - self.floor_y), 2)

    def add_platform(self, platform):
        self.platforms.append(platform)
