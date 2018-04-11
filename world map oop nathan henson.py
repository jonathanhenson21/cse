class Room(object):
    def __init__(self, name, description, items, north, south, east, west):
        self.name = name
        self.north = north
        self.description = description
        self.items = items
        self.south = south
        self.east = east
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


west_house = Room('The Green House', "Insert description here", None, 'backroom', None, None, 'front_door')
backroom = Room("Green Room", "ITS HAS A LOT OF PLANTS ", None, 'outside', 'west_house', 'side_door', 'outside_west')
SOUTH_HOUSE = Room('blue house', "look old have wood walls and a fireplace", None, 'backroom', None, None, 'front_door')
upstair = Room("2 Floor", "it haves 3 room ", None, 'Hall''wide hall way', 'SOUTH_HOUSE, "next_room', 'down_stair', 'left_roomn')
# room1 = Room()
# BLUE_HOUSE = Room('north', 'south', 'west', 'east')
# room2 = Room()
# EAST_OF_LAKE = Room('north', 'south', 'west', 'east')
# room3 = Room()
# WEST_OF_HOME = Room('north', 'south', 'west', 'east')

current_node = west_house
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)  # change
    print(current_node.description)   # Change
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")