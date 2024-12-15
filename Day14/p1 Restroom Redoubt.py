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


for s in range(100):

    for num in range(len(botp)):
        board[botp[num][1]][botp[num][0]] -= 1
 
        botp[num][0] = (botp[num][0] + botv[num][0]) % tileWidth
        botp[num][1] = (botp[num][1] + botv[num][1]) % tileHeigth

        board[botp[num][1]][botp[num][0]] += 1

q1 = 0
for q1x in range(int(tileHeigth/2)):
    for q1y in range(int(tileWidth/2)):
        if board[q1x][q1y] != 0:
            q1 += board[q1x][q1y]

q2 = 0
for q2x in range(int(tileHeigth/2)):
    for q2y in range(int(tileWidth/2)+1,int(tileWidth)):
        if board[q2x][q2y] != 0:
            q2 += board[q2x][q2y]

q3 = 0
for q3x in range(int(tileHeigth/2)+1,int(tileHeigth)):
    for q3y in range(int(tileWidth/2)):
        if board[q3x][q3y] != 0:
            q3 += board[q3x][q3y]

q4 = 0
for q4x in range(int(tileHeigth/2)+1,int(tileHeigth)):
    for q4y in range(int(tileWidth/2)+1,int(tileWidth)):
        if board[q4x][q4y] != 0:
            q4 += board[q4x][q4y]

print(q1*q2*q3*q4)