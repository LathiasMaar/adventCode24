import re

# Read file data
f = open ('Day03/input.txt','r')
corruptedData = f.read()
f.close()

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
match = re.findall(pattern,corruptedData)

ans = 0
enable = True

for i in match:
    
    if i == "don't()":
        enable = False
    elif i == "do()":
        enable = True
    elif (enable ):
        values = i[4:-1].split(',')
        ans += int(values[0]) * int(values[1])

print(ans)




