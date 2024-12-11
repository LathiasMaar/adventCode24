# Read file data
f = open ('Day11/input_test.txt','r')
startingStones = f.read().split()
f.close()

blink = 25

stones = [int(j) for j in startingStones]

for i in range(blink):
    shift = 0
    for s in range(len(stones)):
        digitn = len(str(stones[s+shift]))
        if stones[s+shift] ==  0:
            stones[s+shift] = 1
        elif digitn % 2 == 0:
            stones.insert( s+shift, int(stones[s+shift] // (10**(digitn/2))) )
            shift += 1
            stones[s+shift] = int(stones[s+shift] % (10**(digitn/2)))
        else:
            stones[s+shift] = stones[s+shift] * 2024

print(len(stones))