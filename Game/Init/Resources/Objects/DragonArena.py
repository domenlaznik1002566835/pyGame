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
        self.background_color = (30, 30, 30)  # Temno ozadje za razlikovanje
        self.player_speed = 1  # Zmanjšana hitrost gibanja za Dragon Areno
        self.player_gravity = gravity / 2  # Zmanjšana gravitacija za Dragon Areno
        self.player_jump_force = 1  # Zmanjšana skok sila za Dragon Areno

    def load_platforms(self):
        # Dodaj platforme specifične za Dragon Areno
        self.add_platform(Platform(300, 500, 200, 50))
        self.add_platform(Platform(700, 300, 200, 100))
        self.add_platform(Platform(1100, 600, 200, 70))

    def draw(self, window):
        # Risanje ozadja
        window.fill(self.background_color)
        # Risanje tal
        pg.draw.line(window, (255, 0, 0), (0, self.height - self.floor_y), (self.width, self.height - self.floor_y), 2)
        # Risanje platform
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
            if player_rect.colliderect(platform_rect) and player.y + player.height == platform.y:
                return True
        return False
