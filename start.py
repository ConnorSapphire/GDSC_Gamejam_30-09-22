import pygame
from pygame.locals import *

# Initialise final static variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOUR = (100, 100, 100)
GAME_NAME = "GAME JAM GAME"

# Setup Pygame display 
gameRunning = True
clock = pygame.time.Clock()
myScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)

# Pygame gameloop
while gameRunning:
    # Set FPS
    clock.tick(FPS)
    # Fill background
    myScreen.fill(BACKGROUND_COLOUR)
    # Update screen
    pygame.display.update()
    # Get input
    for event in pygame.event.get():
        # End game loop upon close button clicked
        if event.type == pygame.QUIT:
            # TODO: Setup save before close if needed
            gameRunning = False
