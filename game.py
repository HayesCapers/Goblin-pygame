
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
	'floor': 290,
	'death_floor': 380
}

background = {
	'x': 0,
	'y': 0
}

holes = {
	'1': [-1900, -1975],
	'2': [-2425, -2530],
	'3': [-4490, -4570]
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
	'speed': 4,
	'jump': 15,
	'health': 100,
	'alive': True
}

# bowser = {
# 	'x': 630,
# 	'y': 295,
# 	'speed': 3,
# 	'health': 100
# }

# shroom = {
# 	'x': 100,
# 	'y': 302,
# 	'speed': 4
# }


goomba = {
	'x': 620,
	'y': 302,
	'speed': 2
}

goomba_1 = {
	'x': 620,
	'y': 302,
	'speed': 2
}

goomba_go = [-240, -1512, -1975, -2644, -3228, -3752, -4620, -10000]

# boo = {
# 	'x': 200,
# 	'y': 200,
# 	'speed': 5
# }


physics = {
	'gravity': 5
}


game_paused = False
game_over = False

goomba_image_timer = 0
move_timer = 0
tick = 0
jump_available = True
screen_size = (screen['width'], screen['height'])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Super Mario")
#Background>>
background_image = pygame.image.load('images/full_background.png')
#Background Scaled>>
background_image_scaled = pygame.transform.scale(background_image, (6544, 743))




#\\\\\\\\\\///////////
#||||MARIO IMAGES||||
#//////////\\\\\\\\\\\
mario_stand = pygame.image.load('./mario_movement_pics/Mario_stand.png')
mario_stand_scale = pygame.transform.scale(mario_stand, (50, 44))
#right mvoement images
mario_move_1_load = pygame.image.load('./mario_movement_pics/mario_move_1.png')
mario_move_1 = pygame.transform.scale(mario_move_1_load, (44, 44))
mario_move_2_load = pygame.image.load('./mario_movement_pics/mario_move_2.png')
mario_move_2 = pygame.transform.scale(mario_move_2_load, (44, 44))
mario_move_3_load = pygame.image.load('./mario_movement_pics/mario_move_3.png')
mario_move_3 = pygame.transform.scale(mario_move_3_load, (44, 44))
#left movement images
mario_left_1_load = pygame.image.load('./mario_movement_pics/mario_move_1_left.png')
mario_left_1 = pygame.transform.scale(mario_left_1_load, (44, 44))
mario_left_2_load = pygame.image.load('./mario_movement_pics/mario_move_2_left.png')
mario_left_2 = pygame.transform.scale(mario_left_2_load, (44, 44))
mario_left_3_load = pygame.image.load('./mario_movement_pics/mario_move_3_left.png')
mario_left_3 = pygame.transform.scale(mario_left_3_load, (44, 44))
#jumping
mario_jump_right_load = pygame.image.load('./mario_movement_pics/mario_jump_right.png')
mario_jump_right = pygame.transform.scale(mario_jump_right_load, (44, 44))
mario_jump_left_load = pygame.image.load('./mario_movement_pics/mario_jump_left.png')
mario_jump_left = pygame.transform.scale(mario_jump_left_load, (44, 44))
#Dead
mario_dead_load = pygame.image.load('./mario_movement_pics/mario_death.png')
mario_dead = pygame.transform.scale(mario_dead_load, (44, 44))
#\\\\\\\\\//////////
#|||ENEMY IMAGES|||
#/////////\\\\\\\\\\

goomba_load_1 = pygame.image.load('./mario_movement_pics/goomba_move_1.png')
goomba_scale_1 = pygame.transform.scale(goomba_load_1, (30, 30))
goomba_load_2 = pygame.image.load('./mario_movement_pics/goomba_move_2.png')
goomba_scale_2 = pygame.transform.scale(goomba_load_2, (30, 30))




#Music and SOund Effects
pygame.mixer.music.load('./sounds/mario_theme.wav')
pygame.mixer.music.play(-1)
power_up_sound = pygame.mixer.Sound('./sounds/smb_powerup.wav')
death_sound = pygame.mixer.Sound('./sounds/smb_mariodie.wav')

#/////////////////////////////////////////////////////
#//////////////////MAIN GAME LOOP////////////////////
#///////////////////////////////////////////////////
game_on = True
# Create the game loop (while 1)
while game_on:
	# print background['x']
	# print tick
	goomba_image_timer += 1
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
			elif event.key == 32: #user hit spacebar
				game_paused = not game_paused
			elif event.key == 114: #user hit r
				game_over = False
				background['x'] = 0
				goomba['x'] = 620
				hero['y'] = screen['floor']
				goomba_go = goomba_go
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
	# for i in holes:
	# 	if (background['x'] < holes[i][1]):
	# 		holes.pop(i)
	#falls down hole
	if (game_over == False):
		if (not game_paused):
			if keys_down['up']:
				if (hero['y'] >= 175) and (jump_available == True):
					hero['y'] -= hero['jump']
				if hero['y'] < 175:
					keys_down['up'] = False
					jump_available = False
			if hero['y'] >= screen['floor']:
				jump_available = True		
			# while (hero['y'] < 290):
			# 	keys_down['up'] = False
			if (hero['y'] < (screen['floor'] - 2)):
				hero['y'] += physics['gravity']



			for i in holes:
				if (background['x'] < holes[i][0]) and (background['x'] > holes[i][1]):
					hero['y'] += physics['gravity']
			#---------HOLE WALLS!!-----------

			for i in holes:	
				if (hero['y'] > screen['floor'] + 20):
					if (background['x'] <= holes[i][1] + 20) and (background['x'] > holes[i][1]-50):
						background['x'] = holes[i][1] + 20

			


			# elif keys_down['down']:
			# 	hero['y'] += hero['speed']
			if keys_down['left']:
				background['x'] += hero['speed']
				move_timer += 1
				if (move_timer > 30):
					move_timer = 0
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
			right_mario = [mario_move_1, mario_move_2, mario_move_3, mario_jump_right]
			left_mario = [mario_left_1, mario_left_2, mario_left_3, mario_jump_left]
			#--------Image selector-------
			def image_selector_mario(timer):
				if game_over == False:
					current_image_right = right_mario[0]
					current_image_left = left_mario[0]
					mario_jump_right_currently = right_mario[3]
					mario_jump_left_currently = left_mario[3]
					if (keys_down['up'] and keys_down['right']):
						return mario_jump_right_currently
					if (keys_down['up'] and keys_down['left']):
						return mario_jump_left_currently

					while (keys_down['right'] == True) and (keys_down['up'] == False):
						if (timer > 0) and (timer <= 10):
							current_image_right = right_mario[0]
						elif (timer < 10) and (timer <= 20):
							current_image_right = right_mario[1]
						elif (timer > 20) and (timer <= 30):
							current_image_right = right_mario[2]
						return current_image_right
					while (keys_down['left'] == True):
						if (timer > 0) and (timer <= 10):
							current_image_left = left_mario[0]
						elif (timer < 10) and (timer <= 20):
							current_image_left = left_mario[1]
						elif (timer > 20) and (timer <= 30):
							current_image_left = left_mario[2]
						return current_image_left

					else:
						timer = 0
						return mario_stand_scale
				elif hero['health'] == 0:
					return mario_dead


				#---------Goomba Move----------


			if background['x'] <= holes['1'][1]:
				if keys_down['right']:
					goomba['speed'] = hero['speed'] + 2
				else:
					goomba['speed'] = 2
				goomba['x'] -= goomba['speed']
				
			
			# if background['x'] <= :
			# 		if keys_down['right']:
			# 			goomba['speed'] = hero['speed'] + 2
			# 		else:
			# 			goomba['speed'] = 2
			# 		goomba['x'] -= goomba['speed']
			# if goomba['x'] == -10:
			# 	goomba['x'] = 620
							

			#ANIMATE GOOMBA
			def goomba_img_selector(timer):
				if (timer >= 0) and (timer < 10):
					return goomba_scale_1
				elif (timer >= 10) and (timer < 20):
					return goomba_scale_2
			if (goomba_image_timer >= 20):
				goomba_image_timer = 0

			




			#-----------DEATH EVENTS------------

			#GOOMBA COLLISON
			distance_from_goomba = fabs(hero['x'] - goomba['x']) + fabs(hero['y'] - goomba['y'])
			if (distance_from_goomba < 20):				
				goomba['x'] = hero['x'] - 15
				hero['y'] = 250
				pygame.mixer.music.stop()
				death_sound.play()
				game_over = True


			if (hero['y'] == screen['death_floor']):
				pygame.mixer.music.stop()
				death_sound.play()	
				game_over = True

	#----------GAME OVER----------

	
	


	


		

	
	
	






		
		
			



	#-----RENDER------
	#blit takes 2 arguments
		#1. what?
		#2.where?
	pygame_screen.blit(background_image_scaled, [background['x'],0])

	#Draw the hero wins on the screen
	font = pygame.font.Font('./images/8_bit_pusab.ttf', 10)
	game_over_font = pygame.font.Font('./images/8_bit_pusab.ttf', 25)
	# if (not game_over):
	# 	wins_text = font.render("Lives: %d" % (hero['health']), False, (0,0,0))
	# 	pygame_screen.blit(wins_text, [100, 35])
	# elif game_over:
	# 	wins_text = font.render("Lives 0", False, (0,0,0))
	# 	pygame_screen.blit(wins_text, [100, 35])

	if (game_over == False):
		wins_text = font.render("Lives: %d" % (hero['health']), False, (0,0,0))
	 	pygame_screen.blit(wins_text, [100, 35])
		if (not game_paused):
		# draw the hero
			pygame_screen.blit(image_selector_mario(move_timer), [hero['x'], hero['y']])
		#Goomba 1
			pygame_screen.blit(goomba_img_selector(goomba_image_timer), [goomba['x'], goomba['y']])
		elif (game_paused):
			pygame_screen.blit(mario_stand_scale, [hero['x'], hero['y']])		
			pygame_screen.blit(goomba_scale_1, [goomba['x'], goomba['y']])
			pause_screen = game_over_font.render("Game Paused", False, (0,0,0))
			to_continue_info = font.render("press space to continue.", False, (0,0,0))
			pygame_screen.blit(pause_screen, [150, 150])
			pygame_screen.blit(to_continue_info, [180, 185])
	if (game_over == True):
		pygame_screen.blit(mario_dead, [hero['x'], hero['y']])
		pygame_screen.blit(goomba_scale_1, [goomba['x'], goomba['y']])
		game_over_text = game_over_font.render("GAME OVER!", False, (0,0,0))
		pygame_screen.blit(game_over_text, [200, 150])



	#draw bowser
	# pygame_screen.blit(bowser_image_scale, [bowser['x'], bowser['y']])

	#draw shroom
	# pygame_screen.blit(shroom_image_scale, [shroom['x'], shroom['y']])

	#draw boo-left
	# pygame_screen.blit(boo_left_scale, [boo['x'], boo['y']])

	#GAME OVER text
	
		



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












