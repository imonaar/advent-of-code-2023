import re

input = open("input.txt").read().splitlines()
nodes_map = {}
direction = list(input[0])
current = "AAA"
steps = 0


for i in input[2:]:
    w = re.split(r"[\W]+", i)
    nodes_map[w[0]] = (w[1], w[2])

while current != 'ZZZ':
    d = direction[steps % len(direction)]
    current = nodes_map[current][0 if d == 'L' else 1]  
    steps += 1  

print(steps)
