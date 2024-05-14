from .Weapon import Weapon
import pygame as pg
from .MeleWeapon import MeleWeapon
from .RangedWeapon import RangedWeapon

class Character:
    def __init__(self, name, health, speed, jump_force, fall_speed, max_jump_count, width, height, sprite):
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
        self.last_shot_time = 0
        self.using_weapon = False
        self.last_hit_time = 0
        self.original_image = pg.image.load(sprite)
        self.image_right = pg.transform.scale(self.original_image, (width, height))
        self.image_left = pg.transform.flip(self.image_right, True, False)
        self.image = self.image_right
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

    def move(self, direction, window_width):
        if direction == 'right':
            if self.x + self.width < window_width:
                self.x += self.speed
            if self.current_weapon != None:
                self.current_weapon.rotation = -1
            self.image = self.image_right
        elif direction == 'left':
            if self.x > 0:
                self.x -= self.speed
            if self.current_weapon != None:
                self.current_weapon.rotation = 1
            self.image = self.image_left

    def jump(self):
        if self.jump_count < self.max_jump_count:
            self.jumping = True
            self.velocity = self.jump_force
            self.jump_multiplier = self.jump_force
            self.jump_count += 1

    def use_weapon(self):
        if isinstance(self.current_weapon, MeleWeapon):
            self.using_weapon = True
            self.last_swing_time = pg.time.get_ticks()
            pg.time.set_timer(pg.USEREVENT + 1, self.current_weapon.speed)
        if isinstance(self.current_weapon, RangedWeapon):
            if pg.time.get_ticks() - self.last_shot_time >= self.current_weapon.shoot_cooldown:
                self.using_weapon = True
                self.last_shot_time = pg.time.get_ticks()
                self.weapons[1].shoot(self.x, self.y)

    def get_hitbox(self):
        return pg.Rect(self.x, self.y, self.width, self.height)