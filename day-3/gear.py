import re
from collections import defaultdict

# with open('input.txt') as f:
#     lines = f.readlines()
#     total = 0

#     w = len(lines[0])
#     lines = [
#         '.' * (w + 2),
#         *[f'.{line.strip()}.' for line in lines],
#         '.' * (w + 2),
#     ]

#     for idx, line in enumerate(lines):
#         if "*" not in line:
#             continue
    

#         for gear in re.finditer(r"\*", line):
#             start = gear.start()

#             if line[start - 1].isdigit() and line[start + 1].isdigit():
#                 st = 0
#                 en = 0
#                 for number in re.finditer(r"\d+", line):
                    
#                     if number.end() == start:
#                         st = number.group()

#                     if number.start() == start + 1:
#                         en = number.group()
                    
#                 total += int(st) * int(en)
                    
            
#             if lines[idx-1][start-1].isdigit() or lines[idx-1][start].isdigit() or lines[idx-1][start+1].isdigit() and lines[idx+1][start-1].isdigit() or lines[idx+1][start].isdigit() or lines[idx+1][start+1].isdigit():
#                 prev = lines[idx-1]
#                 after = lines[idx+1]

#                 for number in re.finditer(r"\d+", prev):
#                     if start >= number.start()-1 and start <= number.end()+1:
#                         prev_number = number.group()
                
#                 for number in re.finditer(r"\d+", after):
#                     if start >= number.start()-1 and start <= number.end()+1:
#                         after_number = number.group()
                
#                 total += (int(prev_number) * int(after_number))
#     print(total)
    

def mul(a, b):
    return a * b

with open('input.txt') as f:
    lines = f.readlines()
    total = 0

    w = len(lines[0])
    lines = [
        '.' * (w + 2),
        *[f'.{line.strip()}.' for line in lines],
        '.' * (w + 2),
    ]

    gears: dict[tuple[int, int], list[int]] = defaultdict(list)

    for line_num, line in enumerate(lines):
        for number in re.finditer(r"\d+", line):
            if "*" in (
                l := lines[line_num - 1][number.start() - 1 : number.end() + 1]
            ):
                assert l.count("*") == 1
                gears[(line_num - 1, number.start() - 1 + l.index("*"))].append(
                    int(number.group())
                )

            if line[number.start() - 1] == "*":
                gears[(line_num, number.start() - 1)].append(int(number.group()))

            if line[number.end()] == "*":
                gears[(line_num, number.end())].append(int(number.group()))

            if "*" in (
                l := lines[line_num + 1][number.start() - 1 : number.end() + 1]
            ):
                assert l.count("*") == 1
                gears[(line_num + 1, number.start() - 1 + l.index("*"))].append(
                    int(number.group())
                )
    
    print(sum([mul(*nums) for nums in gears.values() if len(nums) == 2]))
