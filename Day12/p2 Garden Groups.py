# Read file data
f = open ('Day12/input.txt','r')
gardenPlot = f.read().split()
f.close()

garden = [list(row) for row in gardenPlot]
directions = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]

# -------------------------------------------------------------------------------------
def explore_region(garden, r, c, visited, value):
    
    stack = [(r,c)]
    area = 0 
    perimeter = 0

    while stack:
        x, y = stack.pop()
        if (x,y) in visited:
            continue

        visited.add((x,y))
        area += 1

        neighbors = [False,False,False,False]
        i=0
        for dx, dy in directions:    
            mx, my = x + dx, y + dy
            if (0 <= mx < len(garden) and 0 <= my < len(garden[0])): 
                if (garden[mx][my] == value and (mx,my) not in visited):
                    stack.append((mx,my))  
                if garden[mx][my] == value:
                    neighbors[i] = True
            i+=1

        if not (neighbors[0] or neighbors[1]):
            perimeter += 1
        if not (neighbors[1] or neighbors[2]):
            perimeter += 1
        if not (neighbors[2] or neighbors[3]):
            perimeter += 1
        if not (neighbors[3] or neighbors[0]):
            perimeter += 1

        if (neighbors[0] and neighbors[1] and garden[x-1][y+1] != value):
            perimeter += 1
        if (neighbors[1] and neighbors[2] and garden[x+1][y+1] != value):
            perimeter += 1
        if (neighbors[2] and neighbors[3] and garden[x+1][y-1] != value):
            perimeter += 1
        if (neighbors[3] and neighbors[0] and garden[x-1][y-1] != value):
            perimeter += 1

    print(value, perimeter)

    return area, perimeter

# -------------------------------------------------------------------------------------
def explore_garden(garden):
   
    visited = set()
    plants = {}

    for r in range(len(garden)): 
        for c in range(len(garden[0])):

            if (r,c) not in visited:
                value = garden[r][c]
                area, perimeter = explore_region(garden,r,c,visited,value)    

                if value not in plants:
                    plants[value] = []
                    
                plants[value].append({"area": area, "perimeter":perimeter})
    
    return plants

# -------------------------------------------------------------------------------------
plants = explore_garden(garden)

total = 0
for plant, regions in plants.items():
    for region in regions:
        price = region["area"] * region["perimeter"]
        total += price

print(total)