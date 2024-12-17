# Read file data
f = open('Day17/input.txt', 'r')
programRaw = f.read().split('\n')
f.close()

registers = []
registers.append(int(programRaw[0].replace("Register A: ", "")))
registers.append(int(programRaw[1].replace("Register B: ", "")))
registers.append(int(programRaw[2].replace("Register C: ", "")))
program = (programRaw[4].replace("Program: ", "").split(','))

combo_operand = [0, 1, 2, 3, registers[0], registers[1], registers[2], -1]
out = ""

instr_point = 0

while True:
    
    if instr_point >= len(program):
        break

    # adv instruction
    if program[instr_point] == '0':
        instr_point += 1
        op = combo_operand[int(program[instr_point])]
        if op != -1:
            result = registers[0] // 2**op
            registers[0] = result
        instr_point += 1

    # bxl instruction
    elif program[instr_point] == '1':
        instr_point += 1
        result = registers[1] ^ int(program[instr_point])
        registers[1] = result
        instr_point += 1

    # bst instruction
    elif program[instr_point] == '2':
        instr_point += 1
        op = combo_operand[int(program[instr_point])]
        if op != -1:
            result = op % 8
        registers[1] = result
        instr_point += 1
    
    # jnz instruction
    elif program[instr_point] == '3':
        instr_point += 1
        if registers[0] != 0:
            n_pos = int(program[instr_point])
            instr_point = n_pos
        else:
            instr_point += 1

    # bxc instruction
    elif program[instr_point] == '4':
        instr_point += 1
        result = registers[1] ^ registers[2]
        registers[1] = result
        instr_point += 1
    
    # out instruction
    elif program[instr_point] == '5':
        instr_point += 1
        op = combo_operand[int(program[instr_point])]
        if op != -1:
            result = op % 8
        out += str(result) + ','
        instr_point += 1
    
    # bdv instruction
    elif program[instr_point] == '6':
        instr_point += 1
        op = combo_operand[int(program[instr_point])]
        if op != -1:
            result = registers[0] // 2**op
            registers[1] = result
        instr_point += 1

    # cdv instruction
    elif program[instr_point] == '7':
        instr_point += 1
        op = combo_operand[int(program[instr_point])]
        if op != -1:
            result = registers[0] // 2**op
            registers[2] = result
        instr_point += 1

    combo_operand[4] = registers[0]
    combo_operand[5] = registers[1]
    combo_operand[6] = registers[2]

print(out)



    