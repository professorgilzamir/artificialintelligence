import ga
from eightpuzzle import matrix, print_state
import random
from itertools import groupby

def count_inversions(state):
	c = 0
	for i in range(len(state.data)-1):
		if state.data[i] < state.data[i+1] and  not (state.data[i] == 0 and state.data[i+1]==0):
			c += 1
	return c

def calc_parity(state):
	return count_inversions(state) + state.get_zero_coords()[0]
	
class EightPuzzleEnvironment:
	def __init__(self, initial_state, objective_state, initial_size=10):
		self.initial_size = initial_size
		self.initial_state = initial_state
		self.objective_state = objective_state
		self.parity = calc_parity(self.objective_state)
		if (calc_parity(initial_state) != self.parity):
			raise BaseException("Invalid Configuration: initial state and objective state must have the same parity")

	def is_valid(self, s):
		try:
			p = count_inversions(s) + s.get_zero_coords()[0]
			return ((p % 2) == (self.parity % 2))
		except:
			return False
		
	def init(self):
		pop = []
		for i in range(self.initial_size):
			while (True):
				cp = self.objective_state.data.copy()
				random.shuffle(cp)
				s = matrix(3, 3, cp)
				if self.is_valid(s):
						#print("--------------------------------------")
						#print_state(s)
						pop.append(s)
						break
		return pop
	
	def crossover(self, p1, p2):
		c = random.randrange(0, 8)
		child_data = p1.data[0:c];
		child_data += [x for x in p2.data[c:9] if not x in child_data]
		i = 0
		while len(child_data) < 9:
			if not p2.data[i] in child_data:
				child_data.append(p2.data[i])
			i += 1
		child = matrix(3, 3, child_data)
		if (self.is_valid(child)):
			return child
		return None
		
if __name__ == "__main__":
	env = EightPuzzleEnvironment(matrix(3, 3, [1, 0, 2, 3, 4, 5, 6, 7, 8]), matrix(3,3, [0,1,2,3,4,5,6,7,8]))
	pop = env.init()
	child = env.crossover(env.initial_state, env.objective_state)
	print("State:")
	print_state(env.initial_state)
	print("Objective: ")
	print_state(env.objective_state)
	print(env.is_valid(env.initial_state))
	if (child):
		print("Child:")
		print_state(child)
