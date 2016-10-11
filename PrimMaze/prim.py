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
    def __init__(self, parent_grid, upper):
        self.parent = parent_grid
        self.upper_bound = upper
        self.grid_width = self.parent.grid_width - 2
        self.grid_height = self.parent.grid_height - 2
        self.node_width = math.ceil(self.grid_width / 2)
        self.node_height = math.ceil(self.grid_height / 2)
        self.node_grid = grid(self.node_width, self.node_height)
        self.active_nodes = list()
        self.dead_nodes = list()
        for x in range(0, self.node_width):
            for y in range(0, self.node_height):
                self.node_grid.set_point(x, y, random.randint(1, self.upper_bound))
    def move_point(self, origin, direction):
        if (direction == 1):
            return [origin[0], origin[1] - 1]
        if (direction == 2):
            return [origin[0], origin[1] + 1]
        if (direction == 3):
            return [origin[0] - 1, origin[1]]
        if (direction == 4):
            return [origin[0] + 1, origin[1]]
        return origin
    def get_export_point(self, point):
        return [(point[0] * 2) + 1, (point[1] * 2) + 1]
    def get_surrounding(self, node):
        possible_points = list()
        directions = [1, 2, 3, 4]
        direction_skip = list()
        if (node[0] == 0):
            direction_skip.append(3)
        if (node[0] == self.node_width - 1):
            direction_skip.append(4)
        if (node[1] == 0):
            direction_skip.append(1)
        if (node[1] == self.node_height - 1):
            direction_skip.append(2)
        for single_direction in directions:
            if single_direction in direction_skip:
                continue
            new_point = self.move_point(node, single_direction)
            if new_point in self.active_nodes:
                continue
            possible_points.append(new_point)
        if len(possible_points) == 0:
            self.dead_nodes.append(node)
        return possible_points
    def generate(self):
        start_point = [0, 0]
        self.active_nodes.append(start_point)
        while len(self.active_nodes) < (self.node_width * self.node_height):
            possible_arcs = list()
            for single_node in self.active_nodes:
                if single_node in self.dead_nodes:
                    continue
                for possible_node in self.get_surrounding(single_node):
                    possible_arcs.append(arc(self, single_node, possible_node))
            current_arc = None
            current_min = self.upper_bound + 2
            for single_arc in possible_arcs:
                if single_arc.node_distance < current_min:
                    current_min = single_arc.node_distance
                    current_arc = single_arc
            self.active_nodes.append(current_arc.end)
            actual_point_start = self.get_export_point(current_arc.start)
            actual_point_path = self.move_point(actual_point_start, current_arc.move_dir)
            actual_point_end = self.get_export_point(current_arc.end)
            self.parent.set_point(actual_point_start[0], actual_point_start[1], 1)
            self.parent.set_point(actual_point_path[0], actual_point_path[1], 1)
            self.parent.set_point(actual_point_end[0], actual_point_end[1], 1)
    def display(self):
        for y in range(0, self.parent.grid_height):
            final_line = ""
            for x in range(0, self.parent.grid_width):
                if self.parent.get_point(x, y) == 0:
                    final_line += "#"
                else:
                    final_line += " "
            print(final_line)
class arc:
    def __init__(self, parent_maze, start_node, end_node):
        self.start = start_node
        self.end = end_node
        start_weight = parent_maze.node_grid.get_point(start_node[0], start_node[1])
        end_weight = parent_maze.node_grid.get_point(end_node[0], end_node[1])
        self.node_distance = start_weight - end_weight
        self.move_dir = 0
        # 0 = not set
        # 1 = up
        # 2 = down
        # 3 = left
        # 4 = right
        if (start_node[0] == end_node[0]):
            if (start_node[1] > end_node[1]):
                self.move_dir = 1
            else:
                self.move_dir = 2
        else:
            if (start_node[0] > end_node[0]):
                self.move_dir = 3
            else:
                self.move_dir = 4
max_width = 79
max_height = 25
primary_grid = grid(max_width, max_height)
primary_maze = maze(primary_grid, 1000)
primary_maze.generate()
primary_maze.parent.display()
primary_maze.display()
