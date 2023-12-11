import re
import math

input = open("input.txt").read().splitlines()
nodes_map = {}
direction = list(input[0])
current = "AAA"
steps = 0

for i in input[2:]:
    w = re.split(r"[\W]+", i)
    nodes_map[w[0]] = (w[1], w[2])

def solver(start: str)-> int:
    current = start
    steps = 0
    while not current.endswith('Z'):
        d = direction[steps % len(direction)]
        current = nodes_map[current][0 if d == 'L' else 1]  
        steps += 1
    return steps

result = 1
ends_with_a = [ k for k in nodes_map.keys() if k.endswith('A')]

for k in ends_with_a:
    result = math.lcm(result, solver(k))

print(result)