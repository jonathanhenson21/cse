class Room(object):
    def __init__(self, name, description, items, north, south, east, west, up, down):
        self.name = name
        self.north = north
        self.description = description
        self.items = items
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


west_house = Room('The Green House', " its green ", None, 'backroom', None, None, 'front_door', None, None)
backroom = Room("Green Room", "ITS HAS A LOT OF PLANTS ", None, 'outside', 'road', 'side_door', 'outside_west', None, None)
road = Room('road', "long dirt road", None, 'South', None, None, 'SOUTH_HOUSE', None,  None)
SOUTH_HOUSE = Room('blue house', "look old have wood walls and a fireplace", None, 'backroom', None, None, 'front_door', '2 Floor', None)
upstair = Room("2 Floor", "it haves 3 room ", None, 'Hall''wide hall way', 'SOUTH_HOUSE, "next_room', 'down_stair', 'left_room', None, None)
room1 = Room('1 Room', 'One bed and green walls', None,'wall', 'wall', 'wall', 'hallway', None, None)
BLUE_HOUSE = Room('2 Room', 'two beds two windows', None,'wall''wall with a window', 'wall', 'wall', 'door out the hall', None,None)
EAST_OF_LAKE = Room('lake', '2 boat and a dock', None, 'dock ', 'lake', 'water', 'boat one', None, None)
boat1 = Room('boat1', 'red', None, 'other side', 'other boat', 'lake', None, None, None)
boat2 = Room('boat2', 'blue', None, 'west land', 'underwater', 'lake', 'dock',  None, None)
underwater = Room('uderwater' 'water', None, None, None, None, None, None, None,None)
land = Room('west land', 'has a lot of trees', None, 'Pruplehouse', 'yellow house', 'cave', 'a small house', None, None )
land2 = Room('otherside', 'your on the other dock', None, 'tree', 'buncker', 'go back dock', 'Boat house' ,None,None)
pruplehouse = Room('pruplehouse', 'pruple',None , 'room1', 'room2', 'room3', 'room4', None, None)
cave = Room('cave', 'dark', None, 'back of cave', None, None, None, None, None)
backofcave = Room('cave' 'dark', None, None, None, None, None, None, None, None)
yelow = Room('Yellow house', 'yellow', None, 'room1', 'room2', 'room3', 'room4', None, None)
small = Room('small house', 'very small', None,'room1','Room2','Room3','Room4', None,None)
buncker = Room('buncker', 'very big', None, None, None, None, None, None ,None)
TREE = Room('tree','its a tree',None , None, None, None, None, None, None)
boathouse = Room('boat house', 'its haves boats but its lock', None, None, None, None, None, None, None,)

current_node = west_house
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
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
