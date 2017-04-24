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