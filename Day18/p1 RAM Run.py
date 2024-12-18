import heapq
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
f = open ('Day18/input.txt','r')
byteList = f.read().strip().split('\n')
f.close()

grid_size = 71
falling = 1024

coords = []
i = 0
for byte in byteList:
    if (i == falling):
        break
    x,y = byte.split(',')
    coords.append( (int(x),int(y)) )
    i+=1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def create_map(coords):
    map = []
    for x in range(grid_size):
        map.append([])
        for y in range(grid_size):
            map[x].append('.')
    for byte in coords:
        map[byte[1]][byte[0]] = '#'
    return map

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def heuristic(a, b):
    return ( abs(a[0] - b[0]) + abs(a[1] - b[1]) )


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def get_neighbors(map, node):
    x,y = node
    neighbors = []
    dir = [(0,1),(1,0),(0,-1),(-1,0)]

    for dx,dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
            if map[nx][ny] == '.':
                neighbors.append((nx, ny))
    return neighbors

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def find_path(map, start, goal):
    
    open_set = []
    heapq.heappush(open_set, (0,start))
    came_from = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start,goal)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(map, current):
            neighbor_g_score = g_score[current] + 1

            if neighbor_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = neighbor_g_score
                f_score[neighbor] = neighbor_g_score + heuristic(neighbor, goal)

                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':

    start = (0,0)
    goal = (grid_size-1,grid_size-1)

    map = create_map(coords)
    path = find_path(map, start, goal)


    if path is None:
        pass
    else:
        st = 0
        for step in path:
            map[step[0]][step[1]] = '0'
            st += 1

    print(st-1)