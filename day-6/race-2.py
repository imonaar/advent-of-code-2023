import re
from functools import reduce

def mul(a, b ) -> int:
    return a * b

with open('input.txt') as f:
    lines = f.readlines()

    [time, distance] = lines
    time = int( ''.join(n for n in [number.group() for number in re.finditer(r'\d+', time)]))
    distance = int( ''.join(d for d in  [number.group() for number in re.finditer(r'\d+', distance)]))
    sum = 0;
    
    for i in range(time + 1):
            speed = i
            tim = time - i

            travelled = speed * tim

            if travelled <= distance:
                continue

            sum += 1
    
    print(sum)
    





    
