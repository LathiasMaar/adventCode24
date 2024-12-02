# Read file data
f = open ('Day02/input.txt','r')
unusualData = f.read().split('\n')
f.close()

safeCount = 0

# Checks for the safe reports
def check_safe(lvl):
    dffs = [(lvl[i + 1] - lvl[i]) for i in range(len(lvl) - 1)]
    incr = all(d >= 1 and d <= 3 for d in dffs)
    decr = all(d <= -1 and d >= -3 for d in dffs)
    return (incr or decr)


for line in unusualData:
    report = [int(x) for x in line.split()]

    if check_safe(report):
        safeCount += 1
 

print(safeCount)
