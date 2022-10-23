# Game
# Integrantes
# Bryann Alfaro
# Raul Jimenez
# Donaldo Garcia
from constants import *
from soccer import Soccer
import pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('LOGICA DIFUSA')
# pygame.display.set_icon(pygame.image.load('icon.jpg'))

g = Soccer(screen)
background = pygame.image.load('images/field.jpg').convert()


game_on = True
while game_on:
	screen.blit(background, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
	pygame.event.get()
	pygame.time.delay(SPEED)

	# g.update()
	# g.draw()

	# pygame.display.update()
	pygame.display.flip()
