import heapq

# Read file data
f = open ('Day10/input.txt','r')
topographicMap = f.read().split('\n')
f.close()

map = [list(row) for row in topographicMap]
trailhead_start = []
trailhead_end = []

def get_neighbors(node, map):
    x, y = node

    neighbors = []

    directions = [ (0, 1), (-1, 0),(1, 0), (0, -1) ]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
            neighbors.append((nx, ny))

    return neighbors


def search_path(start, goal, map):  
                  
    open_set = []

    heapq.heappush(open_set, start)

    while open_set:

        current = heapq.heappop(open_set)

        if current[0] == goal[0] and current[1] == goal[1]:
            return True

        for neighbor in get_neighbors(current, map):
            if int(map[neighbor[0]][neighbor[1]]) == int(map[current[0]][current[1]])+1:
                if neighbor not in [i for i in open_set]:
                    heapq.heappush(open_set, neighbor)

    return False


for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == '0':
            trailhead_start.append([r,c])
        elif map[r][c] == '9':
            trailhead_end.append([r,c])


count = 0
for i in trailhead_start:
    for j in trailhead_end:
        if search_path(i, j, map):
            count+=1

print(count)
            