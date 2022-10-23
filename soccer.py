import itertools
import math
from constants import *

class Soccer(object):
	def __init__(self, screen):
		self.screen = screen
		self.draw_player(10, 200)

	def clear(self):
		self.screen.fill((0, 0, 0))

	def pixel(self, x, y, color=WHITE):
		self.screen.set_at((x, y), color)
	
	def big_pixel(self, x, y, color=WHITE):
		# draw a pixel, of size 5x5 pixels with center at (x, y)
		for i, j in itertools.product(range(10), range(10)):
			self.pixel(x+i, y+j, color)

	def copy(self):
		self.last_screen = self.screen.copy()
	
	def draw_player(self, x, y, color=RED):
		self.big_pixel(x, y, color)

	def draw_ball(self, x, y, color=BLACK):
		self.big_pixel(x, y, color)