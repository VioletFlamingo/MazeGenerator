class Maze:
	def __init__(self, width, height, start, finish, paths=None, difficulty=None):
		self.width = width
		self.height = height
		self.start = start
		self.finish = finish
		self.paths = paths
		self.difficulty = difficulty