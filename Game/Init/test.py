import pygame
pygame.init()

# Initialize the joysticks
pygame.joystick.init()

# Get count of joysticks
joystick_count = pygame.joystick.get_count()

# For each joystick
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Joystick event handling
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
        elif event.type == pygame.JOYAXISMOTION:
            print("Joystick axis moved.")

pygame.quit()