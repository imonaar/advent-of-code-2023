import re

with open('input.txt') as f:
    lines = f.readlines();
    lines = [line.strip() for line in lines]
    total = 0

    for idx, line in enumerate(lines):
        line = line.split(':')
        [winning, mine] = line[1].strip().split("|")

        winning = winning.split()
        mine = mine.split()
        
        match = set.intersection(set(winning), set(mine))
        if not match: continue
        print(match)
        
        if len(match) == 1:
            total += 1
            continue
        
        init = 1
        
        for _ in range(len(match) - 1):
            init *=2
        total +=init
    
    print(total)