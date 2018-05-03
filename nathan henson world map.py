class Room(object):
    def __init__(self, name, description, items, north, south, east, west, up, down):
        self.name = name
        self.north = north
        self.description = description
        self.items = items
        self.south = south
        self.east = east
        self.west = west


world_map = {
    'WESTHOUSE': {
        'NAME': 'WEST OF PLACE',
        'DESCRIPTION': 'your in a forest all you can see is trees.',
        'PATHS': {
            'SOUTH': 'SOUTHHOUSE',
            'NORTH': 'NORTHHOUSE',
            'WEST': 'WESTHOUSE0',
            'EAST': 'EASTHOUSE'
        }
    }, 
    'SOUTHHOUSE': {
        'NAME': "South of House",
        'DESCRIPTION': "a blue house with 4 windows and 1 door",
        "PATHS": {
            'WEST': 'BLUEHOUSE'

        }
    },
        'BLUEHOUSE': {
            'NAME': "BLUE OF HOUSE",
            'DESCRIPTION': "your in the living room and you have two paths",
            "PATHS": {
                'NORTH':'EASTOFLAKE'


        }
    },
    'EASTOFLAKE': {
        'NAME': "BY THE LAKE",
        'DESCRIPTION': "all you see is the lake and boats",
        "PATHS": {
            'EAST': 'WESTOFHOME'
        }
    },

'WESTOFHOME': {
        'NAME': "IN THE WOODS",
        'DESCRIPTION': "YOUR BY A YELLOW 2 STORY HOUSE",
        "PATHS": {
            'SOUTH': 'LIVINGROOM',
            'EAST': 'NORTHOFCITYZ',
        }
    }
}
current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']
short_directions = ['n', 's', 'e', 'w']
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
