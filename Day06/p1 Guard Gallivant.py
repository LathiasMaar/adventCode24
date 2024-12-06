import copy

# Read file data
f = open ('Day06/input.txt','r')
mapRaw = f.read().split('\n')
f.close()

map = []
i=0

for row in mapRaw:
    map.append([])
    for tiles in row:
        map[i].append(tiles.split())
    i+=1

def search_guard (map):
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == ['^']:
                return row, col
            elif map[row][col] == ['>']:
                return row, col
            elif map[row][col] == ['<']:
                return row, col
            elif map[row][col] == ['v']:
                return row, col
    print("Guard not found")

def print_map(mp):
    for row in mp:
        print(row)

def move_up (map,x,y):
    px,py = x,y
    map[px][py] = ['.']
    px-=1
    if (px >= 0):
        if map[px][py] != ['#']:
            map[px][py] = ['^']
        else:
            px,py = move_right(map, px+1, py)
    return px,py

def move_down (map,x,y):
    px,py = x,y
    map[px][py] = ['.']
    px+=1
    if(px < len(map)):
        if map[px][py] != ['#']:
            map[px][py] = ['v']
        elif(map[px][py] == ['#']):
            px,py = move_left(map, px-1, py)
    return px,py

def move_right (map,x,y):
    px,py = x,y
    map[px][py] = ['.']
    py+=1
    if py < len(map[0]):
        if map[px][py] != ['#']:
            map[px][py] = ['>']
        elif(map[px][py] == ['#']):
            px,py = move_down(map, px, py-1)
    return px,py

def move_left (map,x,y):
    px,py = x,y
    map[px][py] = ['.']
    py-=1
    if py >= 0:
        if(map[px][py] != ['#']):
            map[px][py] = ['<']
        elif(map[px][py] == ['#']):
            px,py = move_up(map, px, py+1)
    return px,py

def move_fwrd(map, x, y):
    px, py = x, y

    if map[px][py] == ['^']:
        px,py = move_up(map, px, py)
    elif map[px][py] == ['>']:
        px,py = move_right(map, px, py)
    elif map[px][py] == ['<']:
        px,py = move_left(map, px, py)
    elif map[px][py] == ['v']:
        px,py = move_down(map, px, py)

    return map, px, py

def update_path(pth,px,py):
    pth[px][py] = ['X']
    return pth

def calculate_path(pth):
    count = 0
    for row in range(len(pth)):
        for col in range(len(pth[row])):
            if pth[row][col] == ['X']:
                count += 1
    return count

def solve (m):
    px, py = search_guard(m)
    map = copy.deepcopy(m)
    xpth = copy.deepcopy(m)

    while 1:

        if(px < 0 or px >= len(map) or py < 0 or py >= len(map[0])):
            break
        else:
            xpth = update_path(xpth,px,py)

        map, px, py = move_fwrd(map, px, py)

    count = calculate_path(xpth)

    print(count)

solve(map)
