import re
from functools import reduce

def mul(a, b ) -> int:
    return a * b

with open('input.txt') as f:
    lines = f.readlines()

    [time, distance] = lines
    time =  [int(number.group()) for number in re.finditer(r'\d+', time)]
    distance =  [int(number.group()) for number in re.finditer(r'\d+', distance)]

    result = []

    for idx, t in enumerate(time):
        d = distance[idx]
        sum = 0

        for i in range(t+1):
            speed = i
            tim = t - i

            travelled = speed * tim

            if travelled <= d:
                continue

            sum +=1

        result.append(sum)
    
    print(reduce(mul, result))




    