import random


class GeneticAlg:
	def __init__(self, environment, mutationrate=0.001):
		self.population = environment.init()
		self.mutationrate = mutationrate
		self.environment = environment
	
	def fitness(self):
		self.totalfitness = 0
		for chromossome in self.population:
			chromossome.fitness = environment.eval(chromossome)
			self.totalfitness += chromossome.fitness

	def crossover(self, parents):
		children = []
		for p1 in parents:
			for p2 in parents:
				if not p1 == p2:
					r = random.random()
					avg = (p1.fitness + p2.fitness)/(2*self.totalfitness)
					if (r <= avg):
							child = environment.crossover(p1, p2)
							if (child):
								children.append()

	def selection(self):
		parents = []
		self.population.sort(key=lambda ch: ch.fitness)
		r = random.random() * self.totalfitness

		for i in range(len(self.population)):
			ch = self.population[i]
			if (r <= ch.fitness/self.totalfitness):
				parents.append(ch.copy())
		
		return parents

	def mutate(self, chromossomes):
		for ch in chromossomes:
			self.environment.mutate(ch, self.mutationrate)

	def step(self):
		self.fitness()
		parents = self.selection()
		children = self.crossover(parents)
		self.mutate(children)
		self.population = children
