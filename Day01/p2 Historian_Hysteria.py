# Read file data
f = open ('Day01/input.txt','r')
inputList = f.read().split('\n')
f.close()

leftList = []
rightList = []
simil = 0

# Separate the elements in their list
for line in inputList:
    parts = line.split()
    leftList.append(parts[0])
    rightList.append(parts[1])

# Sort the lists
leftList.sort()
rightList.sort()

# Calculate the similarity
for i in range(len(leftList)):
    equivalent = 0
    for j in range(len(rightList)):
        if (leftList[i] == rightList[j]):
            equivalent+=1
        elif (leftList[i] < rightList[j]):
            break
    simil += equivalent * int(leftList[i])

# Show result
print(simil)