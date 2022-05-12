from maze import Maze
import pygame


class App:
	"""
	A class written by James Hughes for handling pygame's rendering of the maze and
	the movement through the maze.

	This class is undocumented beyond this, as there is no need to understand what is
	happening.
	"""
	
	def __init__(self, maze):
		self._running = True
		self._display_surf = None
		self._surfs = {}

		self.maze = Maze(maze)
		self.window_height = len(maze) * 40
		self.window_width = len(maze[0]) * 40
		
		self.on_execute()

	def on_init(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode((self.window_width, self.window_height), pygame.HWSURFACE)
		pygame.display.set_caption('aMaze')

		self._running = True
		self._surfs['p'] = pygame.image.load('./images/curpath.png').convert()
		self._surfs['c'] = pygame.image.load('./images/current.png').convert()
		self._surfs['m'] = pygame.image.load('./images/empty.png').convert()
		self._surfs['E'] = pygame.image.load('./images/end.png').convert()
		self._surfs['f'] = pygame.image.load('./images/endFound.png').convert()
		self._surfs['x'] = pygame.image.load('./images/expath.png').convert()		
		self._surfs[' '] = pygame.image.load('./images/open.png').convert()		
		self._surfs['S'] = pygame.image.load('./images/start.png').convert()				
		self._surfs['#'] = pygame.image.load('./images/wall.png').convert()		

	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False

	def on_loop(self):
		pass

	def on_render(self):
		self._display_surf.fill((0, 0, 0))
		self.maze.draw(self._display_surf, self._surfs)
		pygame.display.flip()

	def on_cleanup(self):
		pygame.display.quit() 
		pygame.quit()

	def on_execute(self):
		if not self.on_init():
			self._running = False

		self.on_render()




