from .Weapon import Weapon
import pygame as pg

class Character:
    def __init__(self, name, health, speed, jump_force, fall_speed, width, height):
        self.name = name
        self.health = health
        self.speed = speed
        self.jump_force = jump_force
        self.fall_speed = fall_speed
        self.width = width
        self.height = height
        self.weapons = []
        self.current_weapon = None
        self.x = 0
        self.y = 0

    def draw(self, window):
        pg.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))
        if self.current_weapon != None:
            self.current_weapon.set_coordinates(self.x, self.y)
            self.current_weapon.draw(window)

    def start(self, x, y):
        self.x = x
        self.y = y

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        if self.current_weapon == None:
            self.current_weapon = weapon

    def change_weapon(self, weapon):
        self.current_weapon = weapon

    def move(self, direction):
        if direction == 'left':
            self.x -= self.speed
            self.current_weapon.rotation = 0
        elif direction == 'right':
            self.x += self.speed
            self.current_weapon.rotation = 1