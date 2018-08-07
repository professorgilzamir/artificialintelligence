'''
=========================================================================
Uma demonstração simples de uso do gradiente de descida em uma
superfície bidimensional.
Autor: Gilzamir F. Gomes (gilzamir@outlook.com, gilzamir@gmail.com)
=========================================================================
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math

#Cria uma figura
fig = plt.figure()
#Crie os eixos do R^3 e define o tipo de projeção
ax = fig.add_subplot(111, projection='3d')


def linspace(i, f, n):
	step = (f-i)/n
	values = []
	v = i
	for i in range(n):
		values.append(v)
		v += step
	values.append(f)
	return values

def prod(u, v):
	p = []
	for i in range(len(u)):
		p.append(u[i] * v[i])
	return p

def sum(u, v):
	p = []
	for i in range(len(u)):
		p.append(u[i] + v[i])
	return p

def sqrt(u):
	p = []
	for i in range(len(u)):
		p.append(math.sqrt(u[i]))
	return p

def sdiv(s, u):
	p = []
	for i in range(len(u)):
		p.append(s/u[i])
	return p

def divs(u, s):
	p = []
	for i in range(len(u)):
		p.append(u[i]/s)
	return p
	
def meshgrid(u, v):
	n = len(u)
	m = len(v)
	rx = []
	ry = []
	for i in range(m):
		rx.append(u.copy())
	for j in range(n):
		ry.append(v.copy())
	return (rx, ry)

# Função a ser minimizada
def f(X, Y):
	return sqrt(sum(prod(X,X), prod(Y,Y)))
	
	
#Gradiente da função a ser minimizada
def gradient(X, Y):
	t = sdiv(1,sqrt(sum(prod(X, X), prod(Y, Y))))
	dx = prod(t, X)
	dy = prod(t, Y)
	sz = sqrt(
	
	
	
prod(x,x) + prod(dy, dy))
	return (divs(dx,sz), divs(dy,sz))

# Construindo os dados
u = linspace(-1.0, 1.0, 100)
v = linspace(-1.0, 1.0, 100)
x, y = meshgrid(u, v)
z = f(x[0], y[0])

#plt.ion()
plt.cla()
# Plota a superficie
ax.plot(x, y, z)
p = [0.5, -0.2, f([0.5], [0.2])[0]]
plt.plot([p[0]], [p[1]], [p[2]], marker='o',markersize=3, color='red')
step_size = 0.05
max_steps = 1000
#INICO::GERA PONTOS AO LONGO DO CAMINHO
for i in range(max_steps):
	dx, dy = gradient([p[0]], [p[1]])
	p[0] = p[0] - step_size * dx
	p[1] = p[1] - step_size * dy
	p[2] = f(p[0], p[1])
	plt.plot([p[0]], [p[1]], [p[2]], marker='o',markersize=3, color='red')
#FIM::GERA PONTOS AO LONGO DO CAMINHO
plt.show() #exibir na tela

