# Read file data
f = open ('Day06/input.txt','r')
mapRaw = f.read().split('\n')
f.close()

# Movement declarations
DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

TURN = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

# Create map 
map = [list(row) for row in mapRaw]

# Find the guard, returns it's position
def search_guard (map):
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] in DIRECTIONS:
                return row, col, map[row][col]
    print("Guard not found")

# Function to print the map in terminal (debugg)
def print_map(mp):
    for row in mp:
        print(row)

def move_guard(map, x, y, dir):

    visited = set()
    while True:
        state = (x, y, dir)
        if state in visited:
            return True
        visited.add(state)

        # Calculate mov
        mvx, mvy = DIRECTIONS[dir]
        px, py = x + mvx, y + mvy

        # Out of bounds
        if not (0 <= px < len(map) and 0 <= py < len(map[0])):
            return False
        
        # Obstacle found, turn
        if map[px][py] == '#':
            dir = TURN[dir]
        else:
            x, y = px, py

def solve_p2(map):
    x_strt, y_strt, dir_strt = search_guard(map)
    loop_count = 0

    # Test every empty tile as an obstacle
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == '.':  
                map[r][c] = '#'

                if move_guard(map, x_strt, y_strt, dir_strt):
                    loop_count += 1

                map[r][c] = '.'

    return loop_count

print(solve_p2(map))