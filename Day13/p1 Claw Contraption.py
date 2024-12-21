# Note: this code it's a brute force solution, it's more efficient to calculate the values
# for b-count directly from the ecuations.Then obtain the a-count.

# Read file data
f = open ('Day13/input.txt','r')
arcade = f.read().strip().split("\n\n")
f.close()

clawMachines = []
count = 0

# Parse input ...............................................................................................
for block in arcade:
    parameter = block.strip().split("\n")
    buttonA = tuple(map(int, parameter[0].split(": ")[1].replace("X+", "").replace("Y+", "").split(", ")))
    buttonB = tuple(map(int, parameter[1].split(": ")[1].replace("X+", "").replace("Y+", "").split(", ")))
    prize = tuple(map(int, parameter[2].split(": ")[1].replace("X=", "").replace("Y=", "").split(", ")))
    
    clawMachines.append([buttonA, buttonB, prize])


for machine in clawMachines:

    stepAx = machine[0][0]
    stepBx = machine[1][0]
    objX = machine[2][0]

    stepAy = machine[0][1]
    stepBy = machine[1][1]
    objY = machine[2][1]

    solution = []

    for i in range(100):

        if (objX - i*stepBx) % stepAx == 0 and (objX - i*stepBx) / stepAx < 100 and not (objX - i*stepBx) < 100:
            cntA = int((objX - i*stepBx) / stepAx)
            cntB = i
            if (cntA * stepAy + cntB * stepBy == objY):
                solution.append((cntA, cntB))

        elif (objX - i*stepAx) % stepBx == 0 and (objX - i*stepAx) / stepBx < 100 and not (objX - i*stepAx) < 100:
            cntA = i
            cntB = int((objX - i*stepAx) / stepBx)
            if (cntA * stepAy + cntB * stepBy == objY):
                solution.append((cntA, cntB))
        
        elif (objY - i*stepBy) % stepAy == 0 and (objY - i*stepBy) / stepAy < 100 and not (objY - i*stepBy) < 100:
            cntA = int((objY - i*stepBy) / stepAy)
            cntB = i
            if (cntA * stepAx + cntB * stepBx == objX):
                solution.append((cntA, cntB))
        
        elif (objY - i*stepAy) % stepBy == 0 and (objY - i*stepAy) / stepBy < 100 and not (objY - i*stepAy) < 100:
            cntA = i
            cntB = int((objY - i*stepAy) / stepBy)
            if (cntA * stepAx + cntB * stepBx == objX):
                solution.append((cntA, cntB))

    count = 0
    for sol in solution:
        count += sol[0]*3 + sol[1]

print(count)

