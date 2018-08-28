import numpy as np

def f(X):
	return (X - np.sqrt(3))**2
	
def grad(X):
	return 2 * (X - np.sqrt(3)) 

if __name__=="__main__":
	step_size = 0.01
	epslon = 0.000001
	p = 0.5
	p0 = float("inf")
	print("Cost: %f"%(p))
	while abs(p-p0) >= epslon:
		p0 = p
		p -= step_size * grad(p)
		print("Cost: %f"%(f(p)))
	print("X: %s"%(p))
