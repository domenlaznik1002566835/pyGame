# Imports
import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Window constraints
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
# Box constraints
BOX_WIDTH = 50
BOX_HEIGHT = 50
BACKGROUND_COLOR = (0, 0, 0)
BOX_COLOR = (255, 165, 0)
# Line constraints
LINE_COLOR = (255, 255, 255)
LINE_WIDTH = 5
# Platforms
PLATFORMS = [(400, WINDOW_HEIGHT - 600, 400, LINE_WIDTH),
             (1200, WINDOW_HEIGHT -400, 300, LINE_WIDTH)]
PLATFORM_COLOR = (255, 255, 255)

# Display window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("RPS")

# Box init position
box_x = 0
box_y = WINDOW_HEIGHT - 200 - BOX_HEIGHT
# Box init velocity
BOX_SPEED = 2
DASH_SPEED = 10
DASH_DURATION = 0.10
JUMP_FORCE = 5
GRAVITY = 0.05
move_left = False
move_right = False
is_jumping = False
jump_count = 0
is_dashing = False
dash_end_time = 0

# Dash variables
last_key_time = 0
last_key = None
DASH_COOLDOWN = 2
last_dash_time = 0

# Game loop
while True:
    window.fill(BACKGROUND_COLOR)

    # Checking end of dash
    if is_dashing and time.time() > dash_end_time:
        is_dashing = False

    # Line
    pygame.draw.line(window, LINE_COLOR, (0, WINDOW_HEIGHT - 200), (WINDOW_WIDTH, WINDOW_HEIGHT - 200), LINE_WIDTH)

    # Platforms
    for platform in PLATFORMS:
        pygame.draw.rect(window, PLATFORM_COLOR, platform)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT] and event.key == last_key and time.time() - last_key_time <= 0.5 and time.time() - last_dash_time >= DASH_COOLDOWN:
                is_dashing = True
                dash_end_time = time.time() + DASH_DURATION
                last_dash_time = time.time()
            last_key = event.key
            last_key_time = time.time()

            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_UP and (not is_jumping or jump_count < 2):
                is_jumping = True
                jump_speed = JUMP_FORCE
                jump_count += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False

    # Box movement
    speed = DASH_SPEED if is_dashing else BOX_SPEED
    if move_left:
        box_x -= speed
        if box_x < 0:
            box_x = WINDOW_WIDTH - BOX_WIDTH
    if move_right:
        box_x += speed
        if box_x + BOX_WIDTH > WINDOW_WIDTH:
            box_x = 0

    # Box jumping and gravity
    if is_jumping or box_y < WINDOW_HEIGHT - 200 - BOX_HEIGHT:
        box_y -= jump_speed
        gravity = 0 if any(pygame.Rect(box_x, box_y + BOX_HEIGHT, BOX_WIDTH, 1).colliderect(platform) for platform in PLATFORMS) else GRAVITY
        jump_speed -= gravity
        for platform in PLATFORMS:
            if pygame.Rect(box_x, box_y, BOX_WIDTH, BOX_HEIGHT).colliderect(platform):
                box_y = platform[1] - BOX_HEIGHT
                is_jumping = False
                jump_count = 0
        if box_y >= WINDOW_HEIGHT - 200 - BOX_HEIGHT:
            box_y = WINDOW_HEIGHT - 200 - BOX_HEIGHT
            is_jumping = False
            jump_count = 0

    # Box
    if is_dashing:
        pygame.draw.rect(window, (0, 255, 0), (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))  # Red color for dashing
    else:
        pygame.draw.rect(window, BOX_COLOR, (box_x, box_y, BOX_WIDTH, BOX_HEIGHT))  # Original color when not dashing

    pygame.display.update()