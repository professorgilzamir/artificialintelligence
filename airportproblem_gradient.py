import numpy as np
import matplotlib.pyplot as plt

X = np.array([0, 1, 1.5, 2.0, 3.0, 4.0, 4.2, 4.5, 5.0, 5.5])
Y = np.array([2, 0, -0.5, 2.0, 1.0, 2.0, 3.4, 2.1, 2.0, 3])

xstate = np.array([0.0, 2.0, 7.0])
ystate = np.array([2.5, 2.5, 4.0])

SIZE=10
NEAREST = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

def get_point(i):
	global xstate
	global ystate
	return (xstate[i], ystate[i])

def set_point(i, vx, vy):
	global xstate
	global ystate
	xstate[i] = vx
	ystate[i] = vy

def dist(i, j):
	c = (X[i], Y[i])
	a = get_point(j)
	return (c[0] - a[0])**2 + (c[1] - a[1])**2
	
def update_nearest():
	for i in range(SIZE):
		d0 = dist(i, 0)
		d1 = dist(i, 1)
		d2 = dist(i, 2)
		if d0 <= d1 and d0 <= d2:
			NEAREST[i]=0
		elif d1 <= d2:
			NEAREST[i] = 1
		else:
			NEAREST[i] = 2

def f():
	C0 = np.argwhere(NEAREST==0)
	C1 = np.argwhere(NEAREST==1)
	C2 = np.argwhere(NEAREST==2)
	if len(C0)>0:
		C0 = C0[0]	
	if len(C1)>0:
		C1 = C1[0]
	if len(C2)>0:
		C2 = C2[0]
	d0 = 0
	d1 = 0
	d2 = 0
	for c in C0:
		d0 += dist(c, 0)
	for c in C1:
		d1 += dist(c, 1)
	for c in C2:
		d2 += dist(c, 2)
	return d0 + d1 + d2
	
def grad(i):	
	C = np.argwhere(NEAREST==i)
	if len(C) > 0:
		C = C[0]
	dx = 0.0
	dy = 0.0
	for c in C:
		dx += (xstate[i] - X[c])
		dy += (ystate[i] - Y[c])
	return (2*dx, 2*dy)

if __name__=="__main__":
	update_nearest()
	step_size = 0.000025
	epslon = 0.000000025
	p = f()
	n = 100000000000000000000
	plt.plot(xstate, ystate, 'bo')
	plt.plot(X, Y, 'bo', color='red')
	print("Cost: %f"%(p))
	while abs(p-n) >= epslon:
		for airport in range(3):
			(gx, gy) = grad(airport)		
			#print("%f, %f "%(gx, gy))
			if gx:
				xstate[airport] -= step_size * gx
				update_nearest()
			if gy:
				ystate[airport] -= step_size * gy
				update_nearest()
		n = p
		p = f()
		print("Cost: %f"%(n))
	print("X: %s"%(xstate))
	print("Y: %s"%(ystate))
	plt.plot(xstate, ystate, 'bo', color='green')
	plt.show()
