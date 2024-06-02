import pygame as pg
from Game.Init.Resources.Objects.Platform import Platform
from Game.Init.Resources.Objects.Arena import Arena

class DragonArena(Arena):  # Inherit from the base Arena class
    def __init__(self, name, width, height, gravity, floor_y, background_image, platform_image):
        super().__init__(name, width, height, gravity, floor_y)
        self.background_image = pg.image.load(background_image)
        self.platform_image = pg.image.load(platform_image)
        self.player_speed = 5  # Increased speed
        self.player_gravity = self.gravity  # Keep gravity consistent
        self.player_jump_force = 15  # Increased jump force

    def load_platforms(self):
        # Add platforms specific to Dragon Arena
        self.add_platform(Platform(300, 500, 200, 50))
        self.add_platform(Platform(700, 300, 200, 100))
        self.add_platform(Platform(1100, 600, 200, 70))

    def draw(self, window):
        # Draw background
        background_scaled = pg.transform.scale(self.background_image, (self.width, self.height))
        window.blit(background_scaled, (0, 0))

        # Draw floor
        pg.draw.line(window, (255, 0, 0), (0, self.height - self.floor_y), (self.width, self.height - self.floor_y), 2)

        # Draw platforms
        for platform in self.platforms:
            platform_rect = pg.Rect(platform.x, platform.y, platform.width, platform.height)
            platform_scaled = pg.transform.scale(self.platform_image, (platform.width, platform.height))
            window.blit(platform_scaled, platform_rect.topleft)

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
