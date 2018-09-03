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
def Error(W1, W2, W3, W4, X, Y):
	return (Y-W1*X**3-W2*X**2-W3*X-W4)**2

#Gradiente da função a ser minimizada
def gradient1(W1, W2, W3, W4, X, Y):
	return 2 * (Y-W1*X**3-W2*X**2-W3*X-W4) * (-1) * (X**3)

def gradient2(W1, W2, W3, W4, X, Y):
	return 2 * (Y-W1*X**3-W2*X**2-W3*X-W4) * (-1) * (X**2)

def gradient3(W1, W2, W3, W4, X, Y):
	return 2 * (Y-W1*X**3-W2*X**2-W3*X-W4) * (-1) * (X**1)

def gradient4(W1, W2, W3, W4, X, Y):
	return 2 * (Y-W1*X**3-W2*X**2-W3*X-W4) * (-1)



#plt.ion()
#plt.cla()
# Plota a superficie
x = []
y = []
with open('AutoInsurSweden.txt', 'r') as f:
	reader = csv.reader(f, delimiter='\t')
	for row in reader:
		if (len(row)>0):
			print(row)
			x.append(int(row[0]))
			y.append(float(row[1].replace(',', '.')))

plt.plot(x, y, 'ro', marker='o', markersize=3, color='red')


x = np.array(x)
y = np.array(y)
w1 = -10.1
w2 = 0.01
w3 = -0.001
w4 = -1.0

maxx = np.max(x)
minx = np.min(x)
maxy = np.max(y)
miny = np.min(y)

x = (x-minx)/(maxx-minx)
y = (y-miny)/(maxy-miny)

STEP_SIZE = 0.01
MAX_STEPS = 10000

for i in range(MAX_STEPS):
	#print(Error(w, x, y))
	erro = np.sum(Error(w1, w2, w3, w4, x, y))/len(x)
	print(erro)
	for j in range(len(x)):
		grad1 = gradient1(w1, w2, w3, w4, x[j], y[j])
		grad2 = gradient2(w1, w2, w3, w4, x[j], y[j])
		grad3 = gradient3(w1, w2, w3, w4, x[j], y[j])
		grad4 = gradient4(w1, w2, w3, w4, x[j], y[j])
		w1 = w1 - STEP_SIZE*grad1
		w2 = w2 - STEP_SIZE*grad2
		w3 = w3 - STEP_SIZE*grad3
		w4 = w4 - STEP_SIZE*grad4

#tx = np.linspace(0.0, 100.0)
#ty = w1 * tx * tx * tx + np.sin(w2*tx)

#plt.plot(tx, ty)

yr = w1 * x**3 + w2 * x**2 + w3 * x + w4
x = x * (maxx - minx) + minx
y = yr * (maxy - miny) + miny

plt.plot(x, y, 'ro', marker='o', markersize=3, color='blue')
plt.show() #exibir na tela
