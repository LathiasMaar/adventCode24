import copy

# Read file data
f = open ('Day08/input.txt','r')
rawMap = f.read().split()
f.close()

def create_map(mRaw):
    return [list(row) for row in mRaw]


def search_antenas(m):
    antennaList = {}
    for r in range(len(m)):
        for c in range(len(m[r])):
            tile = m[r][c]
            if tile != '.':
                if tile not in antennaList:
                    antennaList[tile] = []
                antennaList[tile].append((r,c))

    return antennaList


def calculate_antinodes(map, antennaList):
    

    x_limit = len(map)
    y_limit = len(map[0])
    antinodeMap = copy.deepcopy(map)

    for antenna,coords in antennaList.items():
        for j in range(len(coords)):
            for i in range(len(coords)):
                if i != j:
                    px = coords[i][0] - coords[j][0]
                    py = coords[i][1] - coords[j][1]
                    if (coords[i][0]+px >= 0 and coords[i][0]+px < x_limit and coords[i][1]+py >= 0 and coords[i][1]+py < y_limit):
                        antinodeMap[coords[i][0]+px][coords[i][1]+py] = '#'
    
    return antinodeMap


map = create_map(rawMap)
antennaList = search_antenas(map)
antinodeMap = calculate_antinodes(map, antennaList)

count = 0
for r in antinodeMap:
    for c in r:
        if c == '#':
            count += 1
print(count)


