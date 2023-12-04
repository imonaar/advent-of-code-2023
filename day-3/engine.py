import re


with open('input.txt') as f:
    lines = f.readlines();
    w = len(lines[0])

    total = 0
    symbols = re.compile(r"[^\w.]")

    # pad it out to prevent out of range errors
    lines = [
        '.' * (w + 2),
        *[f'.{line.strip()}.' for line in lines],
        '.' * (w + 2),
    ]

    for idx, line in enumerate(lines):
        for number in re.finditer(r"\d+", line):
            valid = [
                symbols.search(lines[idx-1][number.start()-1:number.end()+ 1]),
                symbols.search(line[number.start()-1]),
                symbols.search(line[number.end()]),
                symbols.search(lines[idx+1][number.start()-1:number.end()+ 1])
            ]

            if any(valid):
                total += int(number.group())
    
    print(total)

