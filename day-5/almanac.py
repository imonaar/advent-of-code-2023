from collections import defaultdict


def mapper(values, map_contents):
    output = []

    for value in values:
        value = int(value) 
        result = None
        
        for content in map_contents:
            content = content.split(' ')
            destination_range_start = int(content[0])
            source_range_start = int(content[1])
            r = int(content[2])

            if value >= source_range_start + r or value < source_range_start:
                continue

            s = value - source_range_start
            result = destination_range_start + s
        if not result:
            result = value

        output.append(result)

    return output

with open('input.txt') as f:
    lines = f.readlines()

    contents = ''.join(lines).split('\n\n')

    my_map = defaultdict(list)
    seeds = contents[0]
    seeds = seeds.split(':')[1].strip().split(' ')

    location = []
    
    for content in contents[1:]:
        content = content.split('\n')
        header = content[0]
        name = header.split(' ')[0].replace('-', '_')

        for item in content[1:]:
            my_map[name].append(item.strip())
    

    soil = mapper(seeds, my_map['seed_to_soil'])
    fertilizer = mapper(soil, my_map['soil_to_fertilizer'])
    water = mapper(fertilizer,my_map["fertilizer_to_water"])
    light = mapper(water, my_map['water_to_light'])
    temperature = mapper(light, my_map['light_to_temperature'])
    humidity = mapper(temperature, my_map['temperature_to_humidity'])
    location = mapper(humidity, my_map['humidity_to_location'])

    print(soil)
    print(fertilizer)
    print(water)
    print(light)
    print(temperature)
    print(humidity)
    print(min(location))

