# Read file data
f = open ('Day04/input.txt','r')
wsearch = f.read().split()
f.close()

target = "XMAS"

def find_word(word, grid):
    l_row, l_col = len(grid), len(grid[0])
    directions = [
        (-1,  -1),      # Diagonal up-left
        (-1, 1),        # Diagonal up-right
        (1, 1),         # Diagonal down-right
        (1, -1),        # Diagonal down-left
    ]
    
    count = 0

    for r in range(len(wsearch)):
        for c in range(len(wsearch[r])):

            if grid[r][c] == word[2]:
                found = True
                for dr, dc in directions:

                    pr1 = r + dr                     #pos row (corner 1)
                    pc1 = c + dc                     #pos col (corner 1)
                    pr2 = r - dr                     #oposite corner
                    pc2 = c - dc                     #oposite corner

                    if not (0 <= pr1 < l_row and 0 <= pc1 < l_col and 0 <= pr2 < l_row and 0 <= pc2 < l_col):
                        found = False
                        break

                    if (grid[pr1][pc1] == word[1] and grid[pr2][pc2] == word[3]):
                        continue
                    elif (grid[pr1][pc1] == word[3] and grid[pr2][pc2] == word[1]):
                        continue
                    else:
                        found = False
                
                if found:
                    count+=1
                        
    return count           


print(find_word(target,wsearch))