import sys
import os
import pygame
import json


class Spritesheet():

	# This needs to retrieve the sprite data from the sprite sheet 
	# and meta data from the corresponding json file

	def __init__(self, filename, folders=[], sprite_size=(0,0), default_color=(0,0,0)):
		
		# Get file directory
		self.directory = sys.path[0]

		if type(folders) == type(""): # This handles tuples of length 1, and strings
			self.directory = os.path.join(self.directory, folders)
		else:						  # This handles larger tuples or lists
			for folder in folders:
				self.directory = os.path.join(self.directory, folder)




		# Get spritesheet location
		self.SS_location = os.path.join(self.directory, filename)




		# Get JSON file location
		if "png" in filename:
			self.JSON_location = self.SS_location.replace("png", "json")
		elif "gif" in filename:
			self.JSON_location = self.SS_location.replace("gif", "json")
		else:
			raise FileNotFoundError(f"No png or gif spritesheet found at {directory}.")	# Raise error if the right file type isn't there



		with open(self.JSON_location) as f:
			self.json = json.load(f)
		f.close()

		try:
			with open(self.JSON_location) as f:
				self.json = json.load(f)
			f.close()
		except:
			raise FileNotFoundError(f"JSON file for file: {filename} not found.")

		


		# Initialize pygame resources - an image and a pygame surface
		try:
			self.spritesheet = pygame.image.load(self.SS_location).convert()
		except:
			raise FileNotFoundError(f"File: {filename} not found.")

		self.sprite_surface = pygame.Surface(sprite_size)
		self.sprite_surface.set_colorkey(default_color)






	def get_sprite(self, char, frame):
		frame_data = self.parse_JSON(char, frame) 	# returns info in the form (x,y,w,h)

		self.sprite_surface.blit(self.spritesheet, (0,0), frame_data)

		return self.sprite_surface



	def parse_JSON(self, char, frame):
		name = f"{char}_{frame}"	# Such that the first frame of char 'a' reads as 'a_0'. This is how I formatted my json file

		x = self.json['frames'][name]['x']
		y = self.json['frames'][name]['y']
		w = self.json['frames'][name]['w']
		h = self.json['frames'][name]['h']

		return (x,y,w,h)
				




#s = SpriteSheet("letters_spritesheet.png", ("graphics"), (25,25), (127,127,127))

