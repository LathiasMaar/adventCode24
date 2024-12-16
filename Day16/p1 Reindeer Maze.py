import heapq
from collections import defaultdict

# Read file data
f = open('Day16/input.txt', 'r')
mapRaw = f.read().strip()
f.close()

# Convert raw map into a 2D grid
map_grid = [list(row) for row in mapRaw.split('\n')]

# Parameters for the 4 possible directions: North, South, West, East
N = (-1, 0)  # Up
S = (1, 0)   # Down
W = (0, -1)  # Left
E = (0, 1)   # Right

# Identifies the start ('S') and goal ('E') positions from the map
def find_start_and_goal(map):
    start = goal = None
    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                goal = (x, y)
    return start, goal

# Given a direction, rotate 90 degrees to the right or left
def rotate_direction(dir, right_turn):
    dirs = [E, S, W, N]  
    ind = dirs.index(dir)
    if right_turn:
        return dirs[(ind + 1) % 4]  
    return dirs[(ind - 1) % 4] 

# Returns true if the tile is transitable (not a wall '#')
def is_valid(map, node):
    px, py = node
    return 0 <= px < len(map) and 0 <= py < len(map[0]) and map[px][py] != '#'

# Dijkstra's algorithm with penalty for turns
def dijkstra(map, start, goal):
    start_state = (start, E)
    queue = [(0, start_state, [start])]

    visited = defaultdict(lambda: float('inf'))
    visited[start_state] = 0

    best_score = float('inf')
    paths = []

    while queue:
        score, state, path_pos = heapq.heappop(queue)
        pos, dir = state

        # Stop if current score is greater than the best score found so far
        if score > best_score:
            break

        # If goal is reached, record the path if it's the best score
        if pos == goal:
            if score <= best_score:
                if score < best_score:
                    paths = []  
                    best_score = score
                paths.append(path_pos)
            continue

        # Move forward in the current direction
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if is_valid(map, new_pos):
            new_state = (new_pos, dir)
            new_score = score + 1
            if new_score < visited[new_state]:
                visited[new_state] = new_score
                new_path = path_pos + [new_pos] 
                heapq.heappush(queue, (new_score, new_state, new_path))

        # Try rotating the direction and moving in the new direction
        for right_turn in [True, False]: 
            new_dir = rotate_direction(dir, right_turn)
            new_state = (pos, new_dir)
            new_score = score + 1000 
            if new_score < visited[new_state]:
                visited[new_state] = new_score
                heapq.heappush(queue, (new_score, new_state, path_pos))
    
    return best_score, paths


if __name__ == '__main__':

    # Find start and goal positions
    start, goal = find_start_and_goal(map_grid)
    
    # Run the dijkstra algorithm
    score, paths = dijkstra(map_grid, start, goal)
    print(score)
