import time
import random
import pygame
from Spritesheet import Spritesheet
from Key import Key


sprite_size = 25
scale = 4
width, height = 800,600
spritesheet_bg_color = (127,127,127)

keys = {}
key_order = []



def main():
	
	mode = 2
	char = get_char(mode)


	pygame.init()

	# open window initialize screen object
	screen = pygame.display.set_mode((width,height))

	# set caption and set background to white
	pygame.display.set_caption("Keeper of the Keys")
	screen.fill((255,255,255))


	# initialize spritesheet object
	spritesheet = Spritesheet("letters_spritesheet.png", ("graphics"), (sprite_size, sprite_size), spritesheet_bg_color)

	# initialize array of all keys being used
	init_keys(mode, spritesheet, sprite_size, scale, (0, 0, 700, 500))



	# combine all of the surface objects. This will need to happen every frame.
	screen = blit_keys(screen)

	# update screen with the now-combined surface objects
	pygame.display.update()



	


	running = True
	while running:

		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == 27: #Escape key
					running = False

				if (event.key >= 97 and event.key <= 122) or (event.key >= 48 and event.key <= 57):
					keys[ chr(event.key) ].press()



		screen.fill((255,255,255))
		screen = blit_keys(screen)
		pygame.display.update()
		

				

	






# scale is in the form (x1, y1, x2, y2)
def init_keys(mode, spritesheet, sprite_size, scale, position_bounds):
	if mode == 0: 
		num = 10
	elif mode == 1: 
		num = 26
	else: 
		num = 36

	list_of_available_chars = list(range(num))



	for i in range(num):

		if i < 26: 
			c = chr(97 + i)				# Use letters for first 26 chars
		else: 
			c = chr(48 + i - 26)		# Use numbers for last 10 chars



		x = random.randint(position_bounds[0], position_bounds[2])
		y = random.randint(position_bounds[1], position_bounds[3])

		rot = random.random() * 90
		rot *= (-1) ** random.randint(1,2)
		

		keys[c] = Key(c, spritesheet, sprite_size, scale, (x,y), rot)





		# This randomizes the order which I draw the letters on the screen
		# I don't want them always drawn in alphabetical order
		r_index = random.randint(0, len(list_of_available_chars)-1)

		# Find the char that goes at this index (i) and update the list so it won't repeat
		ordered_char = list_of_available_chars[ r_index ]
		list_of_available_chars.pop(r_index)

		if ordered_char < 26: 
			c = chr(97 + ordered_char)				# Use letters for first 26 chars
		else: 
			c = chr(48 + ordered_char - 26)			# Use numbers for last 10 chars

		key_order.append( c )			# This list is now a list of all the keys of the chars in a randomized order

	




def blit_keys(screen):
	
	for k in key_order:
		sprite = keys[k].get_sprite()
		screen.blit(sprite, keys[k].get_position())


	return screen





def get_char(mode):

	if mode == 0:
		i = random.randint(0,9)
		return chr(48 + i)

	elif mode == 1:
		i = random.randint(0,25)
		return chr(97 + i)

	elif mode == 2:
		i = random.randint(0,35)
		if i < 26:
			return chr(97 + i)
		else:
			return chr(48 + i - 26)




def get_mode():
	mode = "0"		# 0 = number mode, 1 = alphabet mode, 2 = both

	m = input("\nEnter the mode you would like to play,\n0 = number mode, 1 = alphabet mode, 2 = both\n")

	try:
		m = int(m)

		if m >= 0 and m <= 2:
			return m
		else:
			print("Invalid number.")
			return getMode()
	except:
		print("Invalid character.")
		return getMode()



main()
