#Graficas para miniproyecto
#Integrantes
#Bryann Alfaro
#Raul Jimenez
#Donaldo Garcia
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x_mov = np.arange(0, 400, 1)
y_mov = np.arange(0, 400, 1)


#Posiciones X
izquierda = fuzz.trimf(x_mov, [0, 60, 150])
centrox = fuzz.trimf(x_mov, [120, 170, 240])
derecha = fuzz.trimf(x_mov, [200, 300, 400])

#Posiciones Y
abajo = fuzz.trimf(y_mov, [0, 60 , 150])
centro = fuzz.trimf(y_mov, [120, 170, 240])
arriba = fuzz.trimf(y_mov, [200, 300, 400])


#Pertenencia para encontrar pelota
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 9))

ax0.plot(x_mov, izquierda, 'b', linewidth=1.5, label='Izquierda')
ax0.plot(x_mov, derecha, 'g', linewidth=1.5, label='Derecha')
ax0.plot(x_mov, centrox, 'r', linewidth=1.5, label='Centro')
ax0.set_title('Posicion X')
ax0.legend()

ax1.plot(y_mov, arriba, 'b', linewidth=1.5, label='Arriba')
ax1.plot(y_mov, centro, 'g', linewidth=1.5, label='Centro')
ax1.plot(y_mov, abajo, 'r', linewidth=1.5, label='Abajo')
ax1.set_title('Posicion Y')
ax1.legend()
'''

#Defuzzy para encontrar pelota
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 9))

ax0.plot(x_mov, izquierda, 'b', linewidth=1.5, label='Izquierda')
ax0.plot(x_mov, derecha, 'g', linewidth=1.5, label='Derecha')
ax0.plot(x_mov, centrox, 'r', linewidth=1.5, label='Centro')
ax0.set_title('Movimiento X')
ax0.legend()

ax1.plot(y_mov, arriba, 'b', linewidth=1.5, label='Arriba')
ax1.plot(y_mov, centro, 'g', linewidth=1.5, label='Centro')
ax1.plot(y_mov, abajo, 'r', linewidth=1.5, label='Abajo')
ax1.set_title('Movimiento Y')
ax1.legend()

#Pertenencia para patear pelota

#Posiciones X pelota
izquierda = fuzz.trimf(x_mov, [0, 16, 34])
centro_pelota = fuzz.trimf(x_mov, [25, 30, 70])
derecha = fuzz.trimf(x_mov, [60, 72, 100])

#Posiciones Y pelota
abajo = fuzz.trimf(y_mov, [0, 16 , 34])
centro = fuzz.trimf(y_mov, [25, 30, 70])
arriba_pelota = fuzz.trimf(y_mov, [60, 72, 100])

#Posiciones X porteria
centro_porteria = fuzz.trimf(x_mov, [25, 30, 70])

#Posiciones Y porteria
arriba_porteria = fuzz.trimf(y_mov, [60, 72, 100])

#Defuzzy para fuerza
fuerza = np.arange(0, 100, 1)
suave = fuzz.trimf(fuerza, [0, 16, 34])
centro_fuerza = fuzz.trimf(fuerza, [25, 30, 70]) #cambiar a normal
duro = fuzz.trimf(fuerza, [60, 72, 100])

#Graficar fuerza
fig, (ax0) = plt.subplots(nrows=1, figsize=(8, 9))


ax0.plot(fuerza, suave, 'b', linewidth=1.5, label='Suave')
ax0.plot(fuerza, centro_fuerza, 'g', linewidth=1.5, label='Centro')
ax0.plot(fuerza, duro, 'r', linewidth=1.5, label='Duro')
ax0.set_title('Fuerza pelota')
ax0.legend()

fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 9))

ax0.plot(x_mov, izquierda, 'b', linewidth=1.5, label='Izquierda')
ax0.plot(x_mov, derecha, 'g', linewidth=1.5, label='Derecha')
ax0.plot(x_mov, centrox, 'r', linewidth=1.5, label='Centro')
ax0.set_title('posicion X pelota')
ax0.legend()

ax1.plot(y_mov, arriba, 'b', linewidth=1.5, label='Arriba')
ax1.plot(y_mov, centro, 'g', linewidth=1.5, label='Centro')
ax1.plot(y_mov, abajo, 'r', linewidth=1.5, label='Abajo')
ax1.set_title('posicion Y pelota')
ax1.legend()


ax2.plot(x_mov, centro_porteria, 'r', linewidth=1.5, label='Centro')
ax2.set_title('posicion X porteria')
ax2.legend()

ax3.plot(y_mov, arriba_porteria, 'b', linewidth=1.5, label='Arriba')
ax3.set_title('posicion Y porteria')
ax3.legend()


# Turn off top/right axes
for ax in (ax0, ax1, ax2, ax3):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

'''
plt.tight_layout()
plt.show()