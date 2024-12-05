# Read file data
f = open ('Day05/input.txt','r')
printQueue = f.read().split('\n\n')
f.close()

printRules = printQueue[0].split()
printOrder = printQueue[1].split()

instructions = []
updates = []

ans = 0

def check_rules(page1, page2, rules):
    if page1 == page2:
        return True
    for rule in rules:
        if page1 == rule[0] and page2 == rule[1]:
            return True
        elif page1 == rule[1] and page2 == rule[0]:
            return False
    return False

for i in printRules:
    instructions.append(i.split('|'))

for u in printOrder:
    updates.append(u.split(','))

for page in updates:
    validUpdate = True
    middlePage = page[len(page)//2]

    for num in range(len(page)):

        for check in range(len(page)-num-1):
            if not (check_rules(page[num], page[num+check+1], instructions)):
                validUpdate = False
                break

        if not validUpdate:
            break

    if validUpdate:
            ans += int(middlePage)

print(ans)



