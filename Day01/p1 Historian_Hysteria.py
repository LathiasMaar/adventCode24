# Read file data
f = open ('Day01/input.txt','r')
inputList = f.read().split('\n')
f.close()

leftList = []
rightList = []
dist = 0

# Separate the elements in their list
for line in inputList:
    parts = line.split()
    leftList.append(parts[0])
    rightList.append(parts[1])

# Sort the lists
leftList.sort()
rightList.sort()

# Calculate the distance
for id in range(len(leftList)):
    dist += abs(int(leftList[id]) - int(rightList[id]))

# Show result
print(dist)
