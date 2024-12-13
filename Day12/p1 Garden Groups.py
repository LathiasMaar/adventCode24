# Read file data
f = open ('Day12/input.txt','r')
gardenPlot = f.read().split()
f.close()

garden = [list(row) for row in gardenPlot]
directions = [ (0, 1), (-1, 0),(1, 0), (0, -1) ]

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

        for dx, dy in directions:    
                mx, my = x + dx, y + dy
                if (0 <= mx < len(garden) and 0 <= my < len(garden[0])): 
                    if (garden[mx][my] == value and (mx,my) not in visited):
                        stack.append((mx,my))
                    elif(garden[mx][my] != value):
                        perimeter += 1
                else:
                    perimeter += 1        

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