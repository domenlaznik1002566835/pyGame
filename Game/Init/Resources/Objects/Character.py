import pygame as pg
from .MeleWeapon import MeleWeapon
from .RangedWeapon import RangedWeapon

class Character:
    def __init__(self, name, health, speed, jump_force, fall_speed, max_jump_count, width, height, sprite):
        self.name = name
        self.max_health = health  # Store the maximum health
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
        self.flash_start_time = None
        self.flash_duration = None
        self.flash_alpha_direction = 1
        self.outline_color = (255, 255, 255)  # White outline for better visibility

    def draw(self, window):
        if self.flash_start_time is not None:
            elapsed_time = pg.time.get_ticks() - self.flash_start_time
            if elapsed_time < self.flash_duration:
                alpha = self.image.get_alpha() + 5 * self.flash_alpha_direction
                if alpha > 255:
                    alpha = 255
                    self.flash_alpha_direction = -1
                elif alpha < 0:
                    alpha = 0
                    self.flash_alpha_direction = 1
                self.image.set_alpha(alpha)
            else:
                self.image.set_alpha(255)
                self.flash_start_time = None

        # Draw shadow
        shadow = pg.Surface((self.width, self.height), pg.SRCALPHA)
        shadow.fill((0, 0, 0, 50))  # Lighter shadow for better aesthetics
        window.blit(shadow, (self.x + 10, self.y + 10))

        # Draw outline
        outline_image = self.create_outline(self.image, self.outline_color)
        window.blit(outline_image, (self.x - 1, self.y - 1))  # Slight offset for better outline effect

        window.blit(self.image, (self.x, self.y))
        if self.current_weapon:
            self.current_weapon.draw(window, self.x, self.y, self.height, self.width)

        # Draw health bar
        self.draw_health_bar(window)

    def create_outline(self, image, outline_color):
        mask = pg.mask.from_surface(image)
        outline_image = pg.Surface((self.width + 2, self.height + 2), pg.SRCALPHA)
        outline_image.fill((0, 0, 0, 0))
        mask_outline = mask.outline()
        for point in mask_outline:
            outline_image.set_at((point[0] + 1, point[1] + 1), outline_color)
        outline_image.blit(image, (1, 1))
        return outline_image

    def draw_health_bar(self, window):
        health_ratio = self.health / self.max_health  # Use max_health for ratio calculation
        health_bar_width = self.width * health_ratio
        health_bar = pg.Rect(self.x, self.y - 15, health_bar_width, 7)  # Increased height for better visibility
        bg_bar = pg.Rect(self.x, self.y - 15, self.width, 7)
        pg.draw.rect(window, (255, 0, 0), bg_bar)  # Red background
        pg.draw.rect(window, (0, 255, 0), health_bar)  # Green foreground
        pg.draw.rect(window, (255, 255, 255), bg_bar, 2)  # White border for clarity

    def start(self, x, y, rotation):
        self.x = x
        self.y = y
        self.previous_y = y
        if self.current_weapon:
            self.current_weapon.rotation = rotation

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        if not self.current_weapon:
            self.current_weapon = weapon
            self.rotation = weapon.rotation

    def move(self, direction, window_width, speed=None):
        if speed is None:
            speed = self.speed
        if direction == 'right':
            if self.x + self.width < window_width:
                self.x += speed
            if self.current_weapon:
                self.current_weapon.rotation = -1
            self.image = self.image_right
        elif direction == 'left':
            if self.x > 0:
                self.x -= speed
            if self.current_weapon:
                self.current_weapon.rotation = 1
            self.image = self.image_left

    def jump(self, jump_force=None):
        if jump_force is None:
            jump_force = self.jump_force
        if self.jump_count < self.max_jump_count:
            self.jumping = True
            self.velocity = jump_force
            self.jump_multiplier = jump_force
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

    def flash(self, duration):
        self.flash_start_time = pg.time.get_ticks()
        self.flash_duration = duration
        self.flash_alpha_direction = 1
