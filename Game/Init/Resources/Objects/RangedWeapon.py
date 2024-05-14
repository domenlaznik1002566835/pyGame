from .Weapon import Weapon
from .Projectile import Projectile
import pygame as pg

class RangedWeapon(Weapon):
    def __init__(self, name, damage, width, height, speed, cooldown):
        super().__init__(name, damage, width, height, speed)
        self.shoot_cooldown = cooldown
        self.projectiles = []
        original_image = pg.image.load('Resources/Sprites/Empty.png')
        self.image = pg.transform.scale(original_image, (width, height))

    def shoot(self, x, y):
        self.projectiles.append(Projectile(x, y, self.width, self.height, (255, 255, 255), self.rotation, self.speed))

    def draw_projectiles(self, window, screen_width):
        for projectile in self.projectiles:
            projectile.draw(window)
            projectile.fly(screen_width)
            if projectile.x < 0 or projectile.x > screen_width:
                self.projectiles.remove(projectile)

    def draw(self, window, x, y, height, width):
        x_change = self.coordinates[0]
        y_change = self.coordinates[1]
        if self.rotation == 1:
            self.x = x - x_change - self.width
            self.y = y - y_change - self.height // 2
            window.blit(pg.transform.flip(self.image, True, False), (x - x_change - self.width, y - y_change - self.height//2))
        elif self.rotation == -1:
            self.x = x + width + x_change
            self.y = y - y_change - self.height // 2
            window.blit(self.image, (x + width + x_change, y - y_change - self.height//2))