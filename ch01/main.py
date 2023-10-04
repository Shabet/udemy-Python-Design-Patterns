import pygame

# Initilize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the background color
background_color = (255, 255, 255)

# Run the game loop
running = True
while running:
    # Fiil the screen with the background color
    screen.fill(background_color)

    # Draw a red rectangle at (100, 1400) with a size of (200, 2000)
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200))

    # Update the display
    pygame.display.flip()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()