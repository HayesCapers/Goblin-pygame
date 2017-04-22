
# Include pygame which we got from pip
import pygame
import time
from math import fabs
#get random module
from random import randint

# In order to use pygame, we have to use init
pygame.init()


# Create a screen with a size
screen = {
	'height': 385,
	'width': 600,
	'floor': 290
}

background = {
	'x': 0,
	'y': 0
}

keys = {
	'right': 275,
	'left': 276,
	'up': 273,
	'down': 274
}

keys_down = {
	'right': False,
	'left': False,
	'up': False,
	'down': False
}

hero = {
	'x': 200,
	'y': 290,
	'speed': 5,
	'wins': 0,
	'health': 100,
	'alive': True
}

bowser = {
	'x': 500,
	'y': 295,
	'speed': 3,
	'health': 100
}

shroom = {
	'x': 100,
	'y': 302,
	'speed': 4
}

boo = {
	'x': 200,
	'y': 200,
	'speed': 5
}

physics = {
	'gravity': 5
}





move_timer = 0
tick = 0
death_time = 0
screen_size = (screen['width'], screen['height'])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
#Background>>
background_image = pygame.image.load('images/full_background.png')
#Background Scaled>>
background_image_scaled = pygame.transform.scale(background_image, (6544, 743))
hero_image = pygame.image.load('images/mario.png')
bowser_image = pygame.image.load('images/bowser.png')
hero_image_scale = pygame.transform.scale(hero_image, (32, 32))
bowser_image_scale = pygame.transform.scale(bowser_image, (35, 32))
shroom_image = pygame.image.load('images/mario_shroom.png')
shroom_image_scale = pygame.transform.scale(shroom_image, (24, 24))
boo_left = pygame.image.load('./images/boo.gif')
boo_left_scale = pygame.transform.scale(boo_left, (35, 35))
mario_stand = pygame.image.load('./mario_movement_pics/Mario_stand.png')
mario_stand_scale = pygame.transform.scale(mario_stand, (44, 44))
mario_move_1_load = pygame.image.load('./mario_movement_pics/mario_move_1.png')
mario_move_1 = pygame.transform.scale(mario_move_1_load, (44, 44))
mario_move_2_load = pygame.image.load('./mario_movement_pics/mario_move_2.png')
mario_move_2 = pygame.transform.scale(mario_move_2_load, (44, 44))
mario_move_3_load = pygame.image.load('./mario_movement_pics/mario_move_3.png')
mario_move_3 = pygame.transform.scale(mario_move_3_load, (44, 44))



#Music and SOund Effects
# pygame.mixer.music.load('./sounds/mario_01.wav')
# pygame.mixer.music.play(-1)
power_up_sound = pygame.mixer.Sound('./sounds/smb_powerup.wav')
death_sound = pygame.mixer.Sound('./sounds/smb_mariodie.wav')

#/////////////////////////////////////////////////////
#//////////////////MAIN GAME LOOP////////////////////
#///////////////////////////////////////////////////
game_on = True
# Create the game loop (while 1)
while game_on:
	tick += 1
	#We are inside the main game loop. this will run whikelthe gam is on
	#------EVENTS-----

	for event in pygame.event.get():
		# Add a quit event (requires sys)
		#Looping throough all events that happened this game loop cycle
		if event.type == pygame.QUIT:
			#USER CLICKED ON RED X TO LEAVE GAME
			game_on = False
			#Updates boolean, so pygame can escape loop
		elif event.type == pygame.KEYDOWN:
			if event.key == keys['up']:
				keys_down['up'] = True					
			elif event.key == keys['down']:
				keys_down['down'] = True
			elif event.key == keys['left']:
				keys_down['left'] = True
			elif event.key == keys['right']:
				keys_down['right'] = True
			# print event.key
		elif event.type == pygame.KEYUP:
			if event.key == keys['up']:
				keys_down['up'] = False
			elif event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
			elif event.key == keys['right']:
				keys_down['right'] = False				

#----------MARIO MOVEMENT----------
	if keys_down['up']:
		while (keys_down['up'] == True):
			if (hero['y'] >= 175):
				hero['y'] -= hero['speed']
			else:
				keys_down['up'] = False
	# while (hero['y'] < 290):
	# 	keys_down['up'] = False
	if (hero['y'] < (screen['floor'] - 2)):
		hero['y'] += physics['gravity']

	# elif keys_down['down']:
	# 	hero['y'] += hero['speed']
	if keys_down['left']:
		background['x'] += hero['speed']
		#Screen loop left -> right
		# if (hero['x'] <= (-30)):
		# 	hero['x'] = screen['width']
	elif keys_down['right']:
		background['x'] -= hero['speed']
		move_timer += 1
		if (move_timer > 30): 
			move_timer = 0
		#Screen loop right -> left	
		# if (hero['x'] >= screen['width'] + 10):
		# 	hero['x'] = 0

	#---------MARIO ANIMATE---------
	displayed_mario = [mario_move_1, mario_move_2, mario_move_3]
	
	#--------Image selector-------
	def image_selector(timer):
		current_image = displayed_mario[0]
		while (keys_down['right'] == True):
			if (timer > 0) and (timer <= 10):
				current_image = displayed_mario[0]
			elif (timer < 10) and (timer <= 20):
				current_image = displayed_mario[1]
			elif (timer > 20) and (timer <= 30):
				current_image = displayed_mario[2]
			return current_image
		if (keys_down['right'] == False):
			timer = 0
			return mario_stand_scale
		

	#COLLISON + MOVEMENT BOWSER
	distance_between = fabs(hero['x'] - bowser['x']) + fabs(hero['y'] - bowser['y'])
	if (hero['health'] <= 0):
		bowser['x'] = -100
	elif (distance_between < 20):
		#the hero and bowser are touching!
		# print ("Collison!!!")
		#generate a random X > 0, X < screen['width']
		# rand_x = randint(0, screen['width'])
		# if (rand_x == hero['x']):
		# 	rand_x += 100
		# bowser['x'] = rand_x
		hero['health'] -= 25
		if (hero['health'] == 0):
			death_time = tick
	else:	
		if (bowser['x'] >= screen['width'] + 10):
			bowser['x'] = 0
			bowser['speed'] += 1
		else:
			bowser['x'] += bowser['speed']

	#COLLISON SHROOM
	distance_from_shroom = fabs(hero['x'] - shroom['x']) + fabs(hero['y'] - shroom['y'])
	if (hero['health'] <= 0):
		shroom['x'] = -100
	elif (distance_from_shroom < 20):
		# random_x = randint(0, screen['width'])
		# if (random_x == hero['x']):
		# 	random_x += 100
		# shroom['x'] = rand_x
		hero['health'] += 5
		shroom['x'] = hero['x'] - 15
		power_up_sound.play()
	else:
		if (shroom['x'] <= 10):
			shroom['x'] = screen['width']
		else:
			shroom['x'] -= shroom['speed']

	#Collison BOOOO
	distance_from_boo = fabs(hero['x'] - boo['x']) + fabs(hero['y'] - boo['y'])
	if (distance_from_boo < 20):
		# random_x = randint(0, screen['width'])
		# if (random_x == hero['x']):
		# 	random_x += 100
		# shroom['x'] = rand_x
		hero['health'] -= 20
		boo['x'] = hero['x'] - 20
	else:
		if (boo['x'] <= 10):
			boo['x'] = screen['width']
		else:
			boo['x'] -= boo['speed']

	#--------Mario DEAD!---------
	
	






		
		
			



	#-----RENDER------
	#blit takes 2 arguments
		#1. what?
		#2.where?
	pygame_screen.blit(background_image_scaled, [background['x'],0])

	#Draw the hero wins on the screen
	font = pygame.font.Font('./images/8_bit_pusab.ttf', 10)
	game_over_font = pygame.font.Font('./images/8_bit_pusab.ttf', 25)
	if (hero['health'] > 0):
		wins_text = font.render("Health: %d" % (hero['health']), False, (0,0,0))
		pygame_screen.blit(wins_text, [100, 35])
	else:
		wins_text = font.render("Health: 0", False, (0,0,0))
		pygame_screen.blit(wins_text, [100, 35])


	# draw the hero
	pygame_screen.blit(image_selector(move_timer), [hero['x'], hero['y']])

	#draw bowser
	# pygame_screen.blit(bowser_image_scale, [bowser['x'], bowser['y']])

	#draw shroom
	# pygame_screen.blit(shroom_image_scale, [shroom['x'], shroom['y']])

	#draw boo-left
	pygame_screen.blit(boo_left_scale, [boo['x'], boo['y']])

	#GAME OVER text
	if (hero['health'] <= 0):
		game_over_text = game_over_font.render("GAME OVER!", False, (0,0,0))
		pygame_screen.blit(game_over_text, [200, 150])



	pygame.display.flip()
# Screen.fill (pass bg_color)
# Flip the screen and start ove4
	









#--------bowser movement----------
# max_time = 1
		# start_time = time.time()
		# while (time.time() - start_time <= max_time):
	# 	direciton_selector = randint(1, 4)
	# 	if (direciton_selector == 1):
	# 		bowser['y'] -= bowser['speed']
	# 		# direciton_selector = randint(1,3)
	# 	elif (direciton_selector == 2):
	# 		bowser['x'] += bowser['speed']
	# 		# direciton_selector = randint(1,4)
	# 		# while(direciton_selector == 3):
	# 		# 	direciton_selector = randint(1, 4)
	# 	elif (direciton_selector == 3):
	# 		bowser['x'] -= bowser['speed']
	# 		# direciton_selector = randint(1,4)
	# 		# while(direciton_selector == 2):
	# 		# 	direciton_selector = randint(1, 4)
	# 	elif (direciton_selector == 4):
	# 		bowser['y'] += bowser['speed']
	# 		# direciton_selector = randint(2,4)
			
	# if (bowser['x'] >= screen['width']-100):
	# 	bowser['x'] = 100
	# if (bowser['x'] <= 100):
	# 	bowser['x'] = screen['width']-100
	# if (bowser['y'] >= screen['height']-100):
	# 	bowser['y'] = 100
	# if (bowser['y'] <= 100):
	# 	bowser['y'] = screen['height']-100


##---------BOWSER MOVEMENT ATTEMPT 2---------
	# 	ran_x = randint(0, screen['width'])
	# 	ran_y = randint(0, screen['height'])
	# 	ran_location = (ran_x, ran_y)
	# 	bowser_location = (bowser['x'], bowser['y'])
	# 	if (bowser_location != ran_location):
	# 		bowser['x'] += bowser['speed']
	# 		bowser['y'] += bowser['speed']
	# 	elif (bowser_location == ran_location):
	# 		ran_x = randint(0, screen['width'])
	# 		ran_y = randint(0, screen['height'])






#generate a random Y > 0, Y < screen['height']
# rand_y = randint(0, screen['height'])
# bowser['y'] = rand_y












