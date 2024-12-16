# Read file data
f = open ('Day15/input.txt','r')
input = f.read().strip()
map, robotMoveList  = input.split("\n\n")
map = map.split('\n')
f.close()

robotPos = (0,0)

DIR = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
    '\n': (0,0)
}

board = []
for x in range(len(map)):
    board.append([])
    for y in range(len(map[1])):
        board[x].append(map[x][y])
        if (map[x][y] == '@'):
            robotPos = [x,y]


for mov in robotMoveList:
    
    x, y = robotPos[0], robotPos[1]
    mx, my = DIR[mov]
    px, py = x + mx, y + my

    if board[px][py] == '#':
        continue

    elif board[px][py] == '.':
        board[x][y] = '.'
        robotPos[0] += mx 
        robotPos[1] += my 
        board[px][py] = '@'

    elif board[px][py] == 'O':
        mov = False
        ox, oy = px, py
        while board[ox+mx][oy+my] != '#' and ox + mx < len(map)-1 and oy + my < len(map[1]) :
            ox, oy = ox + mx, oy + my
            if board[ox][oy] == '.':
                mov = True
                break

        if mov:
            board[ox][oy] = 'O'
            while ox - mx != px and oy - my != py:
                ox -= mx 
                oy -= my 
                board[ox][oy] = 'O'
            board[x][y] = '.'
            robotPos[0] += mx 
            robotPos[1] += my 
            board[px][py] = '@'
            
sum = 0
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == 'O':
            sum += r*100 + c

print(sum)

