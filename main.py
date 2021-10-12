import time
import random
import pygame


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']


def main():
	#mode = getMode()
	mode = 1

	# get random character for player to guess
	char = getChar(mode)



	# window width and height
	width, height = 800,600

	# initialize pygame
	pygame.init()

	# create screen object
	# make screen object show up on computer screen
	screen = pygame.display.set_mode((width,height))

	# set caption and set background to white
	pygame.display.set_caption("Keeper of the Keys")
	screen.fill((255,255,255))




	# create a font object
	# first parameter is the font file
	# which is contained in pygame
	# second parameter is the font size
	font = pygame.font.SysFont('consolas', 96)

	# create text surface object using font object
	# first parameter is the text
	# second parameter is antialias (True/False)
	# third parameter is color
	text = font.render(char.upper(), True, (0,0,0))

	# get text screen rectangle and center it
	textRect = text.get_rect()
	textRect.center = (width//2, height//2)

	# combine text screen and new text rectangle object
	screen.blit(text, textRect)

	# update screen now with text on it
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
					if chr(event.key) == char:

						char = getChar(mode)
						screen.fill((255,255,255))
						text = font.render(char.upper(), True, (0,0,0))
						screen.blit(text, textRect)



		pygame.display.update()

				

	







def getChar(mode):

	if mode == 0:
		i = random.randint(0,9)
		return numbers[i]
	elif mode == 1:
		i = random.randint(0,25)
		return letters[i]
	elif mode == 2:
		i = random.randint(0,35)
		if i < 26:
			return letters[i]
		else:
			return numbers[i-26]




def getMode():
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