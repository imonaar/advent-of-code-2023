from functools import reduce

def mul(a, b):
    return a * b

with open('input.txt') as f:
    sum = 0
    for line in f.readlines():
        line = line.strip()
        [_, choices] = line.split(':')
        
        choices = choices.split(';')
        mininum = {}

        for choice in choices:
            s = choice.split(',')
            
            for k in s:
                k = k.strip()
                [count, color] = k.split(' ')

                if color in mininum:
                    if mininum[color] < int(count):
                        mininum[color] = int(count)
                else:
                    mininum[color] = int(count)
        power = reduce(mul, list(mininum.values()), 1)
        sum += power
    print(sum)