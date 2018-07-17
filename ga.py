import random

class Chromossome:
	def __init__(self, data, fitness=0.0):
		self.data = data
		self.fitness = fitness
	
	def len(self):
		return len(self.data)
		
	def copy(self):
		c = Chromossome(self.data.copy(), self.fitness)
		return c
		
class GeneticAlg:
	def __init__(self, environment, mutationrate=0.001):
		self.population = environment.init()
		self.mutationrate = mutationrate
		self.environment = environment
		random.seed()
	
	def update_fitness(self):
		self.totalfitness = 0
		for chromossome in self.population:
			chromossome.fitness = self.environment.fitness(chromossome)
			self.totalfitness += chromossome.fitness
		self.population.sort(key=lambda x: x.fitness)

	def step(self):
		novapop = []
		n = len(self.population)
		for i in range(n):
			p1 = None
			p2 = None
			k = n-1
			j = -1
			acm = 0
			max = 0
			while not (p1 and p2):
				r = random.random()
				ch = self.population[k]
				acm += ch.fitness/self.totalfitness
				if (r <= acm):
					if not p1:
						p1 = ch.copy()
						j = k
					elif j != k:
						p2 = ch.copy()
						break
				k -= 1
				if k < 0:
					k = n-1
				max += 1
				if (max > 10000):
					break
			if (p1 and p2):
				ch1 = self.environment.crossover(p1, p2)
				self.environment.mutate(ch1, self.mutationrate)
				novapop.append(ch1)
		self.population = novapop
