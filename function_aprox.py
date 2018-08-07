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
plt.show() #exibir na tela
