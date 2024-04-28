# Imports
import pygame
import sys
import time
import json

# Load configuration
with open('../Resources/constraints.json') as f:
    constrains = json.load(f)

# Loading constraints
# Screen
WINDOW_WIDTH = constrains['WINDOW_WIDTH']
WINDOW_HEIGHT = constrains['WINDOW_HEIGHT']
BACKGROUND_COLOR = constrains['BACKGROUND_COLOR']
# Platforms
LINE_COLOR = constrains['LINE_COLOR']
LINE_WIDTH = constrains['LINE_WIDTH']
PLATFORMS = constrains['PLATFORMS']
PLATFORM_COLOR = constrains['PLATFORM_COLOR']
# Player 1
PLAYER1_WIDTH = constrains['PLAYER1_WIDTH']
PLAYER1_HEIGHT = constrains['PLAYER1_HEIGHT']
PLAYER1_COLOR = constrains['PLAYER1_COLOR']
PLAYER1_SPEED = constrains['PLAYER1_SPEED']
PLAYER1_JUMP_FORCE = constrains['PLAYER1_JUMP_FORCE']
PLAYER1_FALL_SPEED = constrains['PLAYER1_FALL_SPEED']
PLAYER1_GRAVITY = constrains['PLAYER1_GRAVITY']
PLAYER1_START_X = PLAYER1_WIDTH + 500
PLAYER1_START_Y = WINDOW_HEIGHT - 200 - PLAYER1_HEIGHT
# Player 2
PLAYER2_WIDTH = constrains['PLAYER2_WIDTH']
PLAYER2_HEIGHT = constrains['PLAYER2_HEIGHT']
PLAYER2_COLOR = constrains['PLAYER2_COLOR']
PLAYER2_SPEED = constrains['PLAYER2_SPEED']
PLAYER2_JUMP_FORCE = constrains['PLAYER2_JUMP_FORCE']
PLAYER2_FALL_SPEED = constrains['PLAYER2_FALL_SPEED']
PLAYER2_GRAVITY = constrains['PLAYER2_GRAVITY']
PLAYER2_START_X = WINDOW_WIDTH - PLAYER2_WIDTH - 500
PLAYER2_START_Y = WINDOW_HEIGHT - 200 - PLAYER2_HEIGHT
# Sword
SWORD_SIZE = constrains['SWORD_SIZE']

# Initialize Pygame
pygame.init()

# Draw the players
player1 = pygame.Rect(PLAYER1_START_X, PLAYER1_START_Y, PLAYER1_WIDTH, PLAYER1_HEIGHT)
player2 = pygame.Rect(PLAYER2_START_X, PLAYER2_START_Y, PLAYER2_WIDTH, PLAYER2_HEIGHT)

# Create a screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Movement variables
player1_jumping = False
player1_falling = False
player2_jumping = False
player2_falling = False

# Sword variables
player1_sword = pygame.Rect(PLAYER1_START_X + PLAYER1_WIDTH + 10, PLAYER1_START_Y - SWORD_SIZE - 10, SWORD_SIZE, SWORD_SIZE)
player2_sword = pygame.Rect(PLAYER2_START_X - 10, PLAYER2_START_Y - SWORD_SIZE - 10, SWORD_SIZE, SWORD_SIZE)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Player 1 movement
            if event.key == pygame.K_w:
                player1_jumping = True
                player1_jump_speed = PLAYER1_JUMP_FORCE
            # Player 2 movement
            if event.key == pygame.K_UP:
                player2_jumping = True
                player2_jump_speed = PLAYER2_JUMP_FORCE

    keys = pygame.key.get_pressed()

    # Player 1 movement
    if keys[pygame.K_a] and player1.x - PLAYER1_SPEED > 0:
        player1.x -= PLAYER1_SPEED
        player1_sword.x = player1.x - SWORD_SIZE - 10
    if keys[pygame.K_d] and player1.x + PLAYER1_WIDTH + PLAYER1_SPEED < WINDOW_WIDTH:
        player1.x += PLAYER1_SPEED
        player1_sword.x = player1.x + PLAYER1_WIDTH + 10

    # Player 2 movement
    if keys[pygame.K_LEFT] and player2.x - PLAYER2_SPEED > 0:
        player2.x -= PLAYER2_SPEED
        player2_sword.x = player2.x - SWORD_SIZE - 10
    if keys[pygame.K_RIGHT] and player2.x + PLAYER2_WIDTH + PLAYER2_SPEED < WINDOW_WIDTH:
        player2.x += PLAYER2_SPEED
        player2_sword.x = player2.x + PLAYER2_WIDTH + 10

    # Player 1 jump
    if player1_jumping:
        player1.y -= player1_jump_speed
        player1_sword.y = player1.y - SWORD_SIZE - 10
        gravity = PLAYER1_GRAVITY
        player1_jump_speed -= gravity
        if player1.y >= WINDOW_HEIGHT - 200 - PLAYER1_HEIGHT:
            player1.y = WINDOW_HEIGHT - 200 - PLAYER1_HEIGHT
            player1_jumping = False

    # Player 2 jump
    if player2_jumping:
        player2.y -= player2_jump_speed
        player2_sword.y = player2.y - SWORD_SIZE - 10
        gravity = PLAYER2_GRAVITY
        player2_jump_speed -= gravity
        if player2.y >= WINDOW_HEIGHT - 200 - PLAYER2_HEIGHT:
            player2.y = WINDOW_HEIGHT - 200 - PLAYER2_HEIGHT
            player2_jumping = False

    # Screen
    screen.fill(BACKGROUND_COLOR)

    # Floor
    pygame.draw.line(screen, LINE_COLOR, (0, WINDOW_HEIGHT - 200), (WINDOW_WIDTH, WINDOW_HEIGHT - 200), LINE_WIDTH)

    # Swords
    pygame.draw.rect(screen, PLAYER1_COLOR, player1_sword)
    pygame.draw.rect(screen, PLAYER2_COLOR, player2_sword)

    # Draw the players
    pygame.draw.rect(screen, PLAYER1_COLOR, player1)
    pygame.draw.rect(screen, PLAYER2_COLOR, player2)

    # Update the display
    pygame.display.flip()

pygame.quit()