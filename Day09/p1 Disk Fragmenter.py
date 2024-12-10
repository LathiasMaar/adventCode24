# Read file data
f = open ('Day09/input.txt','r')
diskMap = f.read().strip()
f.close()

disk = []
id = 0

for i in range(len(diskMap)):
    if (i % 2 == 0):
        for block in range(int(diskMap[i])):
            disk.append(str(id))
        id += 1
    else:
        for block in range(int(diskMap[i])):
            disk.append('.')


while True:

    emptySpace = -1
    for i in range(len(disk)):
        if disk[i] == '.':
            emptySpace = i
            break
    
    filePos = -1
    for i in range(len(disk)-1, emptySpace, -1):
        if disk[i] != '.':
            filePos = i
            break
    
    if filePos == -1:
        break

    disk[emptySpace] = disk[filePos]
    disk[filePos] = '.'

checksum = 0
for i in range(len(disk)):
    if disk[i] != '.':
        checksum += i * int(disk[i])

print(checksum)

