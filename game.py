
# Include pygame which we got from pip
import pygame

# In order to use pygame, we have to use init
pygame.init()

# Include pygame
# Init pygame
# Create a screen with a size
screen = {
	'height': 512,
	'width': 480
}

screen_size = (screen['height'], screen['width'])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")

game_on = True
# Create the game loop (while 1)
while game_on:
	#We are inside the main game loop. this will run whikelthe gam is on
	for event in pygame.event.get():
		#Looping throough
		if event.type == pygame.QUIT:
			game_on = False
# Add a quit event (requires sys)
# Screen.fill (pass bg_color)
# Flip the screen and start ove4
