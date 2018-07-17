import ga
from eightpuzzle import matrix, print_state
import random
import math
from ga import GeneticAlg
from ga import Chromossome


class EightQueenEnvironment:
	def __init__(self, initial_size=10):
		self.initial_size = initial_size
		
	def init(self):
		pop = []
		for i in range(self.initial_size):
			ch = Chromossome(random.sample(range(8), 8))
			#print(ch.data)
			pop.append(ch)
		return pop

	def decode(self, state):
		m = matrix(8, 8)
		m.set(state.data[0], 0, 1)
		m.set(state.data[1], 1, 1)
		m.set(state.data[2], 2, 1)
		m.set(state.data[3], 3, 1)
		m.set(state.data[4], 4, 1)
		m.set(state.data[5], 5, 1)
		m.set(state.data[6], 6, 1)
		m.set(state.data[7], 7, 1)
		return m

	def crossover(self, p1, p2):
		c = random.randrange(0, 8)
		child_data = p1.data[0:c] + p2.data[c:8]
		return Chromossome(child_data)
	
	def mutate(self, ch, prob):
		r = random.random()
		if r <= prob:
			a = random.randrange(0, 8)
			b = random.randrange(0, 8)
			ch.data[a] = b

	def fitness(self, ch):
		q = 0
		for i in range(8):
			linha1 = ch.data[i]
			for j in range(8):
				if i != j:
					linha2 = ch.data[j]
					if (linha1 == linha2 or i == j or abs((linha2-linha1)/(i-j)) == 1.0):
						q += 1
		return 28-q;

if __name__ == "__main__":
	ga = GeneticAlg(EightQueenEnvironment(200), 0.0)
	print("Population initial size is %d"%(len(ga.population)))
	for i in range(100):
		ga.update_fitness()	
		ch = ga.population[-1]
		print("%f"%(ch.fitness))
		if (ch.fitness >= 28):
			break
		ga.step()
	ga.update_fitness()
	best_solution = ga.population[-1]
	fen = ga.environment.decode(best_solution)
	print_state(fen)
