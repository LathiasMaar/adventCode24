# Read file data
f = open ('Day13/input.txt','r')
arcade = f.read().strip().split("\n\n")
f.close()

clawMachines = []

# Parse input ...............................................................................................
for block in arcade:
    parameter = block.strip().split("\n")
    buttonA = list(map(int, parameter[0].split(": ")[1].replace("X+", "").replace("Y+", "").split(", ")))
    buttonB = list(map(int, parameter[1].split(": ")[1].replace("X+", "").replace("Y+", "").split(", ")))
    prize = list(map(int, parameter[2].split(": ")[1].replace("X=", "").replace("Y=", "").split(", ")))

    prize[0] += 10000000000000
    prize[1] += 10000000000000
    
    clawMachines.append((buttonA,buttonB,prize))

# Solve the ec. system - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# (i * ax) + (j * bx) = px    ->  i = (px - (j * bx)) / ax
# (i * ay) + (j * by) = py    <______|
#
# (px - (j * bx)) * ay + (j * by * ax) = (py * ax)
# (px * ay) - (j * bx * ay) + (j * by * ax) = (py * ax)
#  j * (by * ax - bx * ay) = (py * ax) - (px * ay)

# From here you can deduce that the number of preses are:
#  j = (py * ax) - (px * ay) / (by * ax - bx * ay)

ans = 0

for machine in clawMachines:
    ax, ay = machine[0]
    bx, by = machine[1]
    px, py = machine[2]

    j = ( py * ax - px * ay ) // (by * ax - bx * ay)
    i = (px - (j * bx)) // ax

    if (i > 0 and j > 0):
        if (i * ax) + (j * bx) == px and (i * ay) + (j * by) == py:
            ans += (i * 3) + j

print(ans)



    