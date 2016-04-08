import maze
import visualisationGenerator

maze = maze.Maze(width=4, height=4, start=(0, 0), finish=(3, 3), paths=[((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (1, 2)), ((1, 2), (0, 2)), ((0, 2), (0, 1)), ((0, 2), (0, 3)), 
((0, 3), (1, 3)), ((1, 3), (2, 3)), ((2, 3), (2, 2)), ((2, 2), (2, 1)), ((2, 1), (2, 0)), ((2, 0), (3, 0)), ((2, 1), (3, 1)), ((3, 1), (3, 2)), ((3, 2), (3, 3))]
)

visualisationGenerator.generate(maze)