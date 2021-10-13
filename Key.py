from Spritesheet import Spritesheet
import pygame


class Key:

	
	def __init__(self, char, spritesheet, sprite_size, scale, pos=(0,0), rot=0.0, wait_length=10):
		self.dimensions = (sprite_size, sprite_size)    # (X,Y) aka (Width, Height)
		self.character = char
		self.position = pos
		self.rotation = rot 						# Rotation is in degrees
		self.scale = sprite_size * scale

		self.spritesheet = spritesheet				# spritesheet object, not the spritesheet file location
		self.frame = 0
		self.wait_progress = 0
		self.wait_length = wait_length

		self.sprite_surface = pygame.Surface(self.dimensions)



	# Simulates this key being pressed
	def press(self):
		self.frame = 1
		self.wait_progress = self.wait_length


	# Get the sprite surface
	# And scale, rotate and update the frame as necessary
	def get_sprite(self):
		self.sprite_surface = self.spritesheet.get_sprite(self.character, self.frame)
		self.sprite_surface = pygame.transform.scale(self.sprite_surface, (self.scale, self.scale))
		self.sprite_surface = pygame.transform.rotate(self.sprite_surface, self.rotation)



		if self.wait_progress == 0:
			if self.frame == 1:
				self.frame = 2
				self.wait_progress = self.wait_length
			elif self.frame == 2:
				self.frame = 0
		elif self.wait_progress >= 0:
			self.wait_progress -= 1


		return self.sprite_surface



	def get_position(self):
		return self.position