# Read file data
f = open ('Day07/input.txt','r')
caliEquation = f.read().split('\n')
f.close()

caliResult = 0

# Move operator
def move_operator(op):
    for i in range(len(op)):
        if op[i] == '+':
            op[i] = '*'
            return op
        if op[i] == '*':
            op[i] = '|'
            return op
        elif op[i] == '|':
            op[i]= '+'
    return op

# Check if equation is true
def evaluate_ecuation(res, values):
    
    val = values.split()
    operator = []

    for operation in range(len(val)-1):
        operator.append('+')

    n = len(operator)

    for comb in range(3**n):
        calc = 0
        for i in range(len(val)-1):
            if i == 0:
                if operator[i] == '+':
                    calc = int(val[i]) + int(val[i+1])
                elif operator[i] == '*':
                    calc = int(val[i]) * int(val[i+1])
                elif operator[i] == '|':
                    calc = int(val[i] + val[i+1])

            else:
                if operator[i] == '+':
                    calc = calc + int(val[i+1])
                elif operator[i] == '*':
                    calc = calc * int(val[i+1])
                elif operator[i] == '|':
                    calc = int(str(calc) + val[i+1] )

        if calc == int(result):
            return True
        else:
            operator = move_operator(operator)

    return False



for ec in caliEquation:
    result = ec.split(':')[0]
    testValues = ec.split(':')[1]

    if evaluate_ecuation(result, testValues):
        caliResult += int(result)
    

print(caliResult)
