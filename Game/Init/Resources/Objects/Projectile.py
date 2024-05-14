import pygame as pg

class Projectile:
    def __init__(self, x, y, width, height, color, direction, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.direction = direction
        self.speed = speed

    def draw(self, window):
        pg.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def fly(self, screen_width):
        if self.direction == 1:
            self.x -= self.speed
        else:
            self.x += self.speed

    def get_hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)