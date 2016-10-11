import math
import random
class grid:
    def __init__(self, width, height):
        self.grid_width = width
        self.grid_height = height
        self.binary_grid = list()
        for i in range(0, self.grid_height):
            self.binary_grid.append([0] * self.grid_width)
    def display(self):
        for y in self.binary_grid:
            item_string = ""
            for x in y:
                item_string += str(x)
            print(item_string)
    def set_point(self, x, y, item):
        self.binary_grid[y][x] = item
    def get_point(self, x, y):
        return self.binary_grid[y][x]
class maze:
    def __init__(self, parent_grid):
        self.parent = parent_grid
        self.grid_width = self.parent.grid_width - 2
        self.grid_height = self.parent.grid_height - 2
        self.node_width = math.ceil(self.grid_width / 2)
        self.node_height = math.ceil(self.grid_height / 2)
        self.node_grid = grid(self.node_width, self.node_height)
        for x in range(0, self.node_width):
            for y in range(0, self.node_height):
                self.node_grid.set_point(x, y, random.randint(1, 1000))
    def generate(self):
        #generate code here (line 62 onwards, https://github.com/lin-e/TotallyInefficientPathfinding/blob/master/Main/PrimsMazeGenerationTest/Program.cs)
max_width = 63
max_height = 21
primary_grid = grid(max_width, max_height)
primary_maze = maze(primary_grid)
primary_maze.node_grid.display()
