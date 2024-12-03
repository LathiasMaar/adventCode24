import re

# Read file data
f = open ('Day03/input.txt','r')
corruptedData = f.read()
f.close()

pattern = r"mul\(\d+,\d+\)"
match = re.findall(pattern,corruptedData)

ans = 0

for i in match:
    values = i[4:-1].split(',')
    ans += int(values[0]) * int(values[1])

print(ans)

