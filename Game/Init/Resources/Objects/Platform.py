import pygame as pg

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pg.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))
