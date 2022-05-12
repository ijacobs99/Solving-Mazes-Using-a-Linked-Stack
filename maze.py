class Maze:
	"""
	A class created by James Hughes to draw a maze.

	This class is undocumented beyond this, as there is no need to understand what is
	happening.
	"""
	
	def __init__(self, maze):
		self.rows = len(maze)
		self.cols = len(maze[0])
		self.maze = maze

	def draw(self, display_surf, surfs):
		for y in range(self.rows):
			for x in range(self.cols):
				display_surf.blit(surfs[self.maze[y][x]], (x * 40, y * 40))
