# Read file data
f = open ('Day04/input_test.txt','r')
wsearch = f.read().split()
f.close()

target = "XMAS"

def find_word(word, grid):
    l_row, l_col = len(grid), len(grid[0])
    directions = [
        (0,  1),        # Right
        (1,  0),        # Down
        (1,  1),        # Diagonal down-right
        (1, -1),        # Diagonal down-left
        (0, -1),        # Left
        (-1, 0),        # Up
        (-1, -1),       # Diagonal up-left
        (-1, 1),        # Diagonal up-right
    ]
    
    count = 0

    for r in range(len(wsearch)):
        for c in range(len(wsearch[r])):
            if grid[r][c] == word[0]:
                for dr, dc in directions:
                    found = True
                    pr, pc = r, c

                    for i in range(1,len(word)):
                        pr += dr
                        pc += dc

                        if not (0 <= pr < l_row and 0 <= pc < l_col) or (grid[pr][pc] != word[i]):
                            found = False
                            break
                    if found:
                        count += 1
                
    return count           


print(find_word(target,wsearch))