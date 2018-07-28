'''
=========================================================================
Uma demonstração simples de uso do gradiente de descida em uma
superfície bidimensional.
Autor: Gilzamir F. Gomes (gilzamir@outlook.com, gilzamir@gmail.com)
=========================================================================
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

#Cria uma figura
fig = plt.figure()
#Crie os eixos do R^3 e define o tipo de projeção
ax = fig.add_subplot(111, projection='3d')

# Função a ser minimizada
def f(X, Y):
	return np.sqrt(X**2 + Y**2)

#Gradiente da função a ser minimizada
def gradient(X, Y):
	t = 1.0/np.sqrt(X**2 + Y**2)
	dx = t * X
	dy = t * Y
	sz = np.sqrt(dx**2 + dy**2)
	return (dx/sz, dy/sz)

# Construindo os dados
u = np.linspace(-1.0, 1.0, 100)
v = np.linspace(-1.0, 1.0, 100)
x, y = np.meshgrid(u, v)
z = f(x, y)

#plt.ion()
plt.cla()
# Plota a superficie
ax.plot_surface(x, y, z, color='b', cmap=cm.coolwarm)
p = np.array([0.5, -0.2, f(0.5, 0.2)])
plt.plot([p[0]], [p[1]], [p[2]], marker='o',markersize=3, color='red')
step_size = 0.05
max_steps = 1000
#INICO::GERA PONTOS AO LONGO DO CAMINHO
for i in range(max_steps):
	dx, dy = gradient(p[0], p[1])
	p[0] = p[0] - step_size * dx
	p[1] = p[1] - step_size * dy
	p[2] = f(p[0], p[1])
	plt.plot([p[0]], [p[1]], [p[2]], marker='o',markersize=3, color='red')
#FIM::GERA PONTOS AO LONGO DO CAMINHO
plt.show() #exibir na tela

