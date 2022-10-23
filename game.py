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

# #Posiciones X
# izquierda = fuzz.trimf(x_mov, [0, 16, 34])
# centrox = fuzz.trimf(x_mov, [25, 30, 70])
# derecha = fuzz.trimf(x_mov, [60, 72, WIDTH])

# #Posiciones Y
# abajo = fuzz.trimf(y_mov, [0, 16 , 34])
# centro = fuzz.trimf(y_mov, [25, 30, 70])
# arriba = fuzz.trimf(y_mov, [60, 72, HEIGHT])


#Posiciones X
# izquierda = fuzz.trimf(x_mov, [0, 10, 50])
# centrox = fuzz.trimf(x_mov, [15, 170, 240])
# derecha = fuzz.trimf(x_mov, [200, 300, 400])

# #Posiciones Y
# abajo = fuzz.trimf(y_mov, [0, 10 , 50])
# centro = fuzz.trimf(y_mov, [15, 170, 240])
# arriba = fuzz.trimf(y_mov, [200, 300, 400])

#Posiciones X
izquierda = fuzz.trimf(x_mov, [0, 10, 150])
centrox = fuzz.trimf(x_mov, [120, 170, 240])
derecha = fuzz.trimf(x_mov, [200, 300, 400])

#Posiciones Y
abajo = fuzz.trimf(y_mov, [0, 10 , 150])
centro = fuzz.trimf(y_mov, [120, 170, 240])
arriba = fuzz.trimf(y_mov, [200, 300, 400])

# find the index diferent of 0 in centrox
izquierda_index = np.array(np.where(izquierda != 0))
centrox_idexes = np.array(np.where(centrox != 0))
derecha_index = np.array(np.where(derecha != 0))

abajo_indexes = np.array(np.where(abajo != 0))
centro_indexes = np.array(np.where(centro != 0))
arriba_indexes = np.array(np.where(arriba != 0))

game_on = True

x_ball = 50
y_ball = 70

x_player = 10
y_player = 200
while game_on:
	screen.blit(background, (0, 0))
	g.draw_ball(x_ball, y_ball)
	g.draw_player(x_player, y_player)

	# find the ball x
	izquierda_level_x_ball = fuzz.interp_membership(x_mov, izquierda, x_ball)
	centrox_level_x_ball = fuzz.interp_membership(x_mov, centrox, x_ball)
	derecha_level_x_ball = fuzz.interp_membership(x_mov, derecha, x_ball)
	# player x
	izquierda_level_x_player = fuzz.interp_membership(x_mov, izquierda, x_player)
	centrox_level_x_player = fuzz.interp_membership(x_mov, centrox, x_player)
	derecha_level_x_player = fuzz.interp_membership(x_mov, derecha, x_player)

	# find the ball y
	abajo_level_y_ball = fuzz.interp_membership(y_mov, abajo, y_ball)
	centro_level_y_ball = fuzz.interp_membership(y_mov, centro, y_ball)
	arriba_level_y_ball = fuzz.interp_membership(y_mov, arriba, y_ball)
	# player y
	abajo_level_y_player = fuzz.interp_membership(y_mov, abajo, y_player)
	centro_level_y_player = fuzz.interp_membership(y_mov, centro, y_player)
	arriba_level_y_player = fuzz.interp_membership(y_mov, arriba, y_player)

	# rules move x
	# Si jx = izquierda y px = izquierda entonces mx = izquierda
	active_rule1 = np.fmin(izquierda_level_x_player, izquierda_level_x_ball)
	move_x_activation1 = np.fmin(active_rule1, izquierda)

	# Si jx = izquierda y px = centro entonces mx = centro
	active_rule2 = np.fmin(izquierda_level_x_player, centrox_level_x_ball)
	move_x_activation2 = np.fmin(active_rule2, centrox)

	# Si jx = izquierda y px derecha entonces mx = derecha
	active_rule3 = np.fmin(izquierda_level_x_player, derecha_level_x_ball)
	move_x_activation3 = np.fmin(active_rule3, derecha)

	# Si jx = centro y px = izquierda entonces mx = izquierda
	active_rule4 = np.fmin(centrox_level_x_player, izquierda_level_x_ball)
	move_x_activation4 = np.fmin(active_rule4, izquierda)

	# Si jx = centro y px = centro entonces mx = centro
	active_rule5 = np.fmin(centrox_level_x_player, centrox_level_x_ball)
	move_x_activation5 = np.fmin(active_rule5, centrox)

	# Si jx = centro y px = derecha entonces mx = derecha
	active_rule6 = np.fmin(centrox_level_x_player, derecha_level_x_ball)
	move_x_activation6 = np.fmin(active_rule6, derecha)

	# Si jx = derecha y px = izquierda entonces mx = izquierda
	active_rule7 = np.fmin(derecha_level_x_player, izquierda_level_x_ball)
	move_x_activation7 = np.fmin(active_rule7, izquierda)

	# Si jx = derecha y px = centro entonces mx = centro
	active_rule8 = np.fmin(derecha_level_x_player, centrox_level_x_ball)
	move_x_activation8 = np.fmin(active_rule8, centrox)

	# Si jx = derecha y px = derecha entonces mx = derecha
	active_rule9 = np.fmin(derecha_level_x_player, derecha_level_x_ball)
	move_x_activation9 = np.fmin(active_rule9, derecha)

	# defuzzification
	aggregated = np.fmax(move_x_activation1, np.fmax(move_x_activation2, np.fmax(move_x_activation3, np.fmax(move_x_activation4, np.fmax(move_x_activation5, np.fmax(move_x_activation6, np.fmax(move_x_activation7, np.fmax(move_x_activation8, move_x_activation9))))))))

	# calculate defuzzified result
	move_x = fuzz.defuzz(x_mov, aggregated, 'centroid')

	# we move the y player because the image is rotated
	y_player = round(move_x)

	# rules move y
	# Si jy = abajo y py = abajo entonces my = abajo
	active_rule1 = np.fmin(abajo_level_y_player, abajo_level_y_ball)
	move_y_activation1 = np.fmin(active_rule1, abajo)

	# Si jy = abajo y py = centro entonces my = centro
	active_rule2 = np.fmin(abajo_level_y_player, centro_level_y_ball)
	move_y_activation2 = np.fmin(active_rule2, centro)

	# Si jy = abajo y py arriba entonces my = arriba
	active_rule3 = np.fmin(abajo_level_y_player, arriba_level_y_ball)
	move_y_activation3 = np.fmin(active_rule3, arriba)

	# Si jy = centro y py = abajo entonces my = abajo
	active_rule4 = np.fmin(centro_level_y_player, abajo_level_y_ball)
	move_y_activation4 = np.fmin(active_rule4, abajo)

	# Si jy = centro y py = centro entonces my = centro
	active_rule5 = np.fmin(centro_level_y_player, centro_level_y_ball)
	move_y_activation5 = np.fmin(active_rule5, centro)

	# Si jy = centro y py = arriba entonces my = arriba
	active_rule6 = np.fmin(centro_level_y_player, arriba_level_y_ball)
	move_y_activation6 = np.fmin(active_rule6, arriba)

	# Si jy = arriba y py = abajo entonces my = abajo
	active_rule7 = np.fmin(arriba_level_y_player, abajo_level_y_ball)
	move_y_activation7 = np.fmin(active_rule7, abajo)

	# Si jy = arriba y py = centro entonces my = centro
	active_rule8 = np.fmin(arriba_level_y_player, centro_level_y_ball)
	move_y_activation8 = np.fmin(active_rule8, centro)

	# Si jy = arriba y py = arriba entonces my = arriba
	active_rule9 = np.fmin(arriba_level_y_player, arriba_level_y_ball)
	move_y_activation9 = np.fmin(active_rule9, arriba)

	# defuzzification
	aggregated = np.fmax(move_y_activation1, np.fmax(move_y_activation2, np.fmax(move_y_activation3, np.fmax(move_y_activation4, np.fmax(move_y_activation5, np.fmax(move_y_activation6, np.fmax(move_y_activation7, np.fmax(move_y_activation8, move_y_activation9))))))))

	# calculate defuzzified result
	move_y = fuzz.defuzz(y_mov, aggregated, 'centroid')

	# we move the x player because the image is rotated
	x_player = round(move_y)

	if (x_player in centrox_idexes and x_ball in centro_indexes) or (x_player in izquierda_index and x_ball in izquierda_index) or (x_player in derecha_index and x_ball in derecha_index):
		x_player += x_ball - x_player
	
	if (y_player in centrox_idexes and y_ball in centro_indexes) or (y_player in izquierda_index and y_ball in izquierda_index) or (y_player in derecha_index and y_ball in derecha_index):
		y_player += y_ball - y_player


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False

	pygame.event.get()
	pygame.time.delay(SPEED)

	# g.update()
	# g.draw()

	# pygame.display.update()
	pygame.display.flip()
