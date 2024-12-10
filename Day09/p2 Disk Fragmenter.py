# Read file data
f = open ('Day09/input.txt','r')
diskMap = f.read().strip()
f.close()

disk = []
id = 0

#Create the file sector map -------------------------------------
for i in range(len(diskMap)):
    if (i % 2 == 0):
        for block in range(int(diskMap[i])):
            disk.append(str(id))
        id += 1
    else:
        for block in range(int(diskMap[i])):
            disk.append('.')


# find a empty space -------------------------------------------
skip = 0
for i in range(len(disk)-1, 0, -1):
    
    pos = i - skip

    if pos < 0:
        break

    if disk[pos] != '.':
        id = disk[pos]
        blockSize = 0
        while disk[pos - blockSize] == id:
            blockSize += 1

        for j in range(len(disk)):
            
            if j > pos - blockSize:
                break

            emptySpaceLen = 0
            while disk[j + emptySpaceLen] == '.' and j + emptySpaceLen < len(disk) -1:
                emptySpaceLen += 1

            if emptySpaceLen >= blockSize:
                for a in range(blockSize):
                    disk[j+a] = disk[pos-a]
                    disk[pos-a] = '.'
                    blockSize = 0 
                break

        skip += blockSize - 1

checksum = 0
for i in range(len(disk)):
    if disk[i] != '.':
        checksum += i * int(disk[i])

print(checksum)

