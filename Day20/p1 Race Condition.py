import heapq
from collections import defaultdict

# Read file data
f = open('Day20/input.txt', 'r')
mapRaw = f.read().strip()
f.close()

# Convert raw map into a 2D grid
map_grid = [list(row) for row in mapRaw.split('\n')]

# Directions: North, South, West, East
N = (-1, 0)
S = (1, 0)
W = (0, -1)
E = (0, 1)
dirs = [E, S, W, N]

# Identify start ('S') and goal ('E') positions in the map
def find_start_and_goal(map_grid):
    start = goal = None
    for x, row in enumerate(map_grid):
        for y, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                goal = (x, y)
    return start, goal

# Returns true if a tile is passable
def is_valid(map_grid, pos):
    x, y = pos
    return 0 <= x < len(map_grid) and 0 <= y < len(map_grid[0]) and map_grid[x][y] != '#'

# Returns true if a wall can be skipped
def is_skipable(map_grid, wall_pos):
    x, y = wall_pos
    for dir in dirs:
        skip_pos = (x + dir[0], y + dir[1])
        if (
            0 <= skip_pos[0] < len(map_grid) and
            0 <= skip_pos[1] < len(map_grid[0]) and
            map_grid[x][y] == '#' and map_grid[skip_pos[0]][skip_pos[1]] == '.'
        ):
            return True
    return False

# Dijkstra's algorithm to calculate path time
def dijkstra(map_grid, start, goal, skip_wall=None):
    queue = [(0, start)] 
    visited = set()
    while queue:
        time, pos = heapq.heappop(queue)

        if pos in visited:
            continue
        visited.add(pos)

        if pos == goal:
            return time  

        for dir in dirs:
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])

            if skip_wall and next_pos == skip_wall:
                heapq.heappush(queue, (time + 1, next_pos))
            elif is_valid(map_grid, next_pos):
                heapq.heappush(queue, (time + 1, next_pos))

    return float('inf')  

# Main function to calculate time savings for each skippable wall
def calculate_savings(map_grid):
    start, goal = find_start_and_goal(map_grid)

    base_time = dijkstra(map_grid, start, goal)

    savings = []
    checked_walls = set()  

    for x, row in enumerate(map_grid):
        for y, cell in enumerate(row):
            if cell == '#' and (x, y) not in checked_walls:

                if is_skipable(map_grid, (x, y)):
                    skip_time = dijkstra(map_grid, start, goal, skip_wall=(x, y))

                    if skip_time < base_time:
                        savings.append(((x, y), base_time - skip_time))

                    checked_walls.add((x, y))
    return savings

if __name__ == '__main__':

    savings = calculate_savings(map_grid)
    
    p = 0 
    for wall, saving in savings:
        if saving >= 100:
            p+=1
    
    print(p)


