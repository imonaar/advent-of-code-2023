with open("input.txt") as f:
    sum = 0
    for reading in f.readlines():
        reading = reading.strip().split(' ')
        reading =[*map(int, reading)]
        total = 0

        while(True): 
            total += reading[-1]
            if reading.count(reading[0]) == len(reading):
                break

            new_arr = []
            for idx in range(len(reading)-1):
                new_arr.append(reading[idx+1] - reading[idx])
            
            reading = new_arr
        sum+=total     
    print(sum)
            
        
        

        