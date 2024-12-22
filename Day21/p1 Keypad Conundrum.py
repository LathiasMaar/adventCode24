from itertools import permutations, product

# Read file data
f = open ('Day21/input.txt','r')
doorCodes = f.read().strip().split("\n")
f.close()

numPad = {
    "7": (0,0), "8": (0,1), "9": (0,2),
    "4": (1,0), "5": (1,1), "6": (1,2),
    "1": (2,0), "2": (2,1), "3": (2,2),
                "0": (3,1), "A": (3,2)
}

dirPad = {
                '^': (0,1), 'A': (0,2),
    '<': (1,0), 'v': (1,1), '>': (1,2)
}

directions = {
    "^": (-1,0), 
    "v": (1, 0), 
    "<": (0,-1), 
    ">": (0, 1)
}


def calculate_paths(code, keypad):

    paths = []
    cur_pos = keypad["A"]

    for c in code:
        next_pos = keypad[c]
        dx = next_pos[0] - cur_pos[0]
        dy = next_pos[1] - cur_pos[1] 

        moves= ""
        if dx > 0:
            moves += "v" * dx
        elif dx < 0:
            moves += "^" * abs(dx)
        if dy > 0:
            moves += ">" * dy
        elif dy < 0:
            moves += "<" * abs(dy)
        
        all_permutations = list(set(["".join(p) + "A" for p in permutations(moves)]))
        
        valid_permutations = []
        for p in all_permutations:
            px,py = cur_pos
            valid = True
            for m in p[:-1]:
                dx,dy = directions[m]
                px += dx
                py += dy
                if not (px,py) in keypad.values():
                    valid = False
                    break
            if valid:
                valid_permutations.append(p)

        paths.append(valid_permutations)
        cur_pos = next_pos
    
    return ["".join(p) for p in product(*paths)]


def solve(code):
    code1 = calculate_paths(code, numPad)
    code2 = []
    for code in code1:
        code2.extend(calculate_paths(code, dirPad))
    code3 = []
    for code in code2:
        code3.extend(calculate_paths(code, dirPad))

    return min(len(x) for x in code3)
        
ans = 0
for code in doorCodes:
    ans += solve(code) * int(code[:-1])

print(ans)
