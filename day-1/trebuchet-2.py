numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('codes.txt', 'r') as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        digits = []

        for idx, ch in enumerate(line):
            if ch.isdigit():
                digits.append(ch)
            for idx_, value in enumerate(numbers):
                if line[idx:].startswith(value):
                    digits.append(str(idx_ + 1))
        
        value = int(digits[0]+digits[-1])
        total += value;

    print(total)
    
 


