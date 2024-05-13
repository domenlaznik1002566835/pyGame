from .Weapon import Weapon
import pygame as pg

class Character:
    def __init__(self, name, health, speed, jump_force, fall_speed, max_jump_count, width, height):
        self.name = name
        self.health = health
        self.speed = speed
        self.jump_force = jump_force
        self.fall_speed = fall_speed
        self.width = width
        self.height = height
        self.weapons = []
        self.current_weapon = None
        self.velocity = 0
        self.jumping = False
        self.max_jump_count = max_jump_count
        self.jump_count = 0
        self.x = 0
        self.y = 0
        self.previous_y = 0
        self.jump_multiplier = self.jump_force
        self.last_swing_time = 0
        self.using_weapon = False
        self.last_hit_time = 0
        original_image = pg.image.load('Resources/Sprites/testCharacter.png')
        self.image = pg.transform.scale(original_image, (width, height))
        self.rotation = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if self.current_weapon != None:
            self.current_weapon.draw(window, self.x, self.y, self.height, self.width)

    def start(self, x, y, rotation):
        self.x = x
        self.y = y
        self.previous_y = y
        if self.current_weapon != None:
            self.current_weapon.rotation = rotation

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        if self.current_weapon == None:
            self.current_weapon = weapon
            self.rotation = weapon.rotation


    def change_weapon(self, weapon):
        self.current_weapon = weapon

    def move(self, direction, window_width):
        if direction == 'right':
            if self.x + self.width < window_width:
                self.x += self.speed
            if self.current_weapon != None:
                self.current_weapon.rotation = -1
        elif direction == 'left':
            if self.x > 0:
                self.x -= self.speed
            if self.current_weapon != None:
                self.current_weapon.rotation = 1

    def jump(self):
        if self.jump_count < self.max_jump_count:
            self.jumping = True
            self.velocity = self.jump_force
            self.jump_multiplier = self.jump_force
            self.jump_count += 1

    def use_weapon(self):
        if self.current_weapon is not None:
            self.using_weapon = True
            self.last_swing_time = pg.time.get_ticks()
            pg.time.set_timer(pg.USEREVENT + 1, self.current_weapon.speed)

    def get_hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)