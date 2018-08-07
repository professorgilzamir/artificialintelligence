'''
=========================================================================
Uma demonstração simples de uso do gradiente de descida em uma
superfície bidimensional.
Autor: Gilzamir F. Gomes (gilzamir@outlook.com, gilzamir@gmail.com)
=========================================================================
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

# Função a ser minimizada
def Error(W, X, Y):
	return (Y-W*X)**2

#Gradiente da função a ser minimizada
def gradient(W, X, Y):
	return 2 * (Y-W * X)*(-X)
	
#plt.ion()
#plt.cla()
# Plota a superficie
x = []
y = []
with open('AutoInsurSweden.txt', 'r') as f:
	reader = csv.reader(f, delimiter='\t')
	for row in reader:
		print(row)
		x.append(int(row[0]))
		y.append(float(row[1].replace(',', '.')))

plt.plot(x, y, 'ro', marker='o', markersize=3, color='red')


x = np.array(x)
y = np.array(y)
w = 0.2

maxx = np.max(x)
minx = np.min(x)
maxy = np.max(y)
miny = np.min(y)

x = (x-minx)/(maxx-minx)
y = (y-miny)/(maxy-miny)

STEP_SIZE = 0.01
MAX_STEPS = 1000

for i in range(MAX_STEPS):
	#print(Error(w, x, y))
	erro = np.sum(Error(w, x, y))/len(x)
	print(erro)
	for j in range(len(x)):
		grad = gradient(w, x[j], y[j])
		w = w - STEP_SIZE*grad

yr = w * x
x = x * (maxx - minx) + minx
yr = yr * (maxy - miny) + miny

plt.plot(x, yr, 'ro', marker='o', markersize=3, color='blue')


'''
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
'''
plt.show() #exibir na tela
