import pygame as pg
from Game.Init.Resources.Objects.Platform import Platform

class DragonArena:
    def __init__(self, name, width, height, gravity, floor_y):
        self.name = name
        self.width = width
        self.height = height
        self.gravity = gravity
        self.floor_y = floor_y
        self.platforms = []
        self.background_color = (30, 30, 30)
        self.player_speed = 1
        self.player_gravity = gravity / 2
        self.player_jump_force = 3

    def load_platforms(self):
        self.add_platform(Platform(300, 500, 200, 50))
        self.add_platform(Platform(700, 300, 200, 100))
        self.add_platform(Platform(1100, 600, 200, 70))

    def draw(self, window):
        window.fill(self.background_color)
        pg.draw.line(window, (255, 0, 0), (0, self.height - self.floor_y), (self.width, self.height - self.floor_y), 2)
        for platform in self.platforms:
            platform.draw(window)

    def add_platform(self, platform):
        self.platforms.append(platform)

    def check_collision(self, player):
        player_rect = pg.Rect(player.x, player.y, player.width, player.height)
        for platform in self.platforms:
            platform_rect = pg.Rect(platform.x, platform.y, platform.width, platform.height)
            if player_rect.colliderect(platform_rect):
                return platform
        return None

    def is_on_platform(self, player):
        player_rect = pg.Rect(player.x, player.y, player.width, player.height)
        for platform in self.platforms:
            platform_rect = pg.Rect(platform.x, platform.y, platform.width, platform.height)
            if player_rect.colliderect(platform_rect) and abs((player.y + player.height) - platform.y) < 10:
                return True
        return False

    def move_down_through_platform(self, player):
        if self.is_on_platform(player):
            player.y += 50
            player.jumping = True
