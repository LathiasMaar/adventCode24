# Read file data
f = open ('Day11/input.txt','r')
startingStones = f.read().split()
f.close()

blink = 75
stones = [int(j) for j in startingStones]

cache = {}

def count_digits(number):
    return len(str(number))

def blink_change(stone, iteration):
    if (stone, iteration) in cache:
        return cache[(stone, iteration)]
    
    if iteration == 0:
        return 1
    else:
        if stone == 0:
            cnt =  blink_change(1, iteration - 1)
        else:
            num_digits = count_digits(stone)
            if num_digits % 2 == 0:
                n1 = int(str(stone)[:num_digits//2])
                n2 = int(str(stone)[num_digits//2:])
                cnt =  blink_change(n1, iteration - 1) + blink_change(n2, iteration - 1)
            else:
                cnt =  blink_change(2024*stone, iteration - 1)

        cache[(stone, iteration)] = cnt
        return cnt

print(sum([blink_change(i, blink) for i in stones]))