# Read file data
f = open ('Day14/input.txt','r')
robotList = f.read().strip().split('\n')
f.close()

tileWidth = 101
tileHeigth = 103

botp = []
botv = []
board = []

for y in range(tileHeigth):
    board.append([])
    for x in range(tileWidth):
        board[y].append(0)

for robot in robotList:
    pos, vel = robot.split(' ')
    pos = pos.replace("p=", "").split(",")
    vel = vel.replace("v=", "").split(",")

    botp.append( [int(pos[0]),int(pos[1])] )
    botv.append( [int(vel[0]),int(vel[1])] )

    board[int(pos[1])][int(pos[0])] += 1

s = 0
while True:

    for num in range(len(botp)):
        board[botp[num][1]][botp[num][0]] -= 1
 
        botp[num][0] = (botp[num][0] + botv[num][0]) % tileWidth
        botp[num][1] = (botp[num][1] + botv[num][1]) % tileHeigth

        board[botp[num][1]][botp[num][0]] += 1

    s += 1
    horizontalLine = 0
    for x in board:
        if sum(1 for y in x if y != 0) > 30:
            horizontalLine += 1

        if horizontalLine == 2:
            print(s)
            break


                

        

    