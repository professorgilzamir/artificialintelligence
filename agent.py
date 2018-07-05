import math

class simple_problem_solver:
	def __init__(self, agent_impl):
		self.agent_impl = agent_impl
		self.state = agent_impl.get_state()
		self.actions = []
	def act(self, percept):
		self.state = self.agent_impl.update_state(percept)
		if (len(self.actions) == 0):
			self.agent_impl.formulate_goal()
			self.agent_impl.formulate_problem()
			self.actions = self.agent_impl.search()
			#print(self.actions)
			if (self.actions==None):
				return None
		
		action = self.actions.pop(0)
		return action

class Node:
	def __init__(self,parent, state, step_cost, action):
		parent_path_cost = 0
		if (parent):
			parent_path_cost = parent.path_cost
		self.state = state
		self.path_cost = parent_path_cost + step_cost
		self.action = action
		self.parent = parent
		
	def solution(self):
		node = self
		actions = []
		while (node != None):
			if (node.action):
				actions.insert(0,node.action)
			node = node.parent
		return actions
		
class agent_impl:
	def __init__():
		pass
	
	def get_state(self):
		return None
		
		
	def update_state(self, percept):
		pass
		
	def formulate_goal(self):
		pass
		
	def formulate_problem(self):
		pass

	def expand(self, node):
		pass
		
	def objective_test(self, goal):
		pass
		
	def search(self):
		pass

	