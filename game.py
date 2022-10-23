# Game
# Integrantes
# Bryann Alfaro
# Raul Jimenez
# Donaldo Garcia
from constants import *
from soccer import Soccer
import numpy as np
import skfuzzy as fuzz
import pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('LOGICA DIFUSA')
# pygame.display.set_icon(pygame.image.load('icon.jpg'))

background = pygame.image.load('images/field.jpg').convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
g = Soccer(screen)

x_mov = np.arange(0, HEIGHT, 1)
y_mov = np.arange(0, WIDTH, 1)

game_on = True
while game_on:
	screen.blit(background, (0, 0))
	g.draw_player(10, 200)
	g.draw_ball(200, 200)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
	pygame.event.get()
	pygame.time.delay(SPEED)

	# g.update()
	# g.draw()

	# pygame.display.update()
	pygame.display.flip()
