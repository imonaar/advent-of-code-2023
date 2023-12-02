with open('input.txt') as f:
    sum_id = 0
    for line in f.readlines():
        line = line.strip()
        [game, choices] = line.split(':')
        [_, id] = game.split(' ')
        id = int(id)
        
        choices = choices.split(';')

        total = {
            'blue': 0,
            'red': 0,
            'green': 0,
        }

        possible = True
        
        for choice in choices:
            s = choice.split(',')
            
            for k in s:
                k = k.strip()
                [count, color] = k.split(' ')
                total[color] = int(count)

            if total['red'] > 12 or total['blue'] > 14 or total['green'] > 13:
                possible = False

        if possible:
            print(line)
            sum_id += id
    
    print(sum_id)