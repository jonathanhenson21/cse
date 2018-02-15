world_map = {
    'WESTHOUSE': {
        'NAME': 'WEST OF PLACE',
        'DESCRIPTION': 'your in a forest all you can see is trees.',
        'PATHS': {
            'SOUTH': 'SOUTHHOUSE',
            'NORTH': 'NORTHHOUSE'
        }
    },
    'SOUTHHOUSE': {
        'NAME': "South of House",
        'DESCRIPTION': "a blue house with 4 windows and 1 door",
        "PATHS": {
            'WEST': 'WESTHOUSE'
        }
    },
    'EASTOFLAKE': {
        'NAME': "BY THE LAKE",
        'DESCRIPTION': "all you see is the lake and boats",
        "PATHS": {
            'EAST': 'EASTOFLAKE'
        }
    }
}

current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']
while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("you cannot go this way")
    else:
        print("command not recognized")
