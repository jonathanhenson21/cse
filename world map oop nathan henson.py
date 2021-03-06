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


west_house = Room('The Green House', "あなたはここであなたの旅を始めるでしょう", 'Back_pack', 'backroom', None, None,
                  'front_door', None, None)
backroom = Room("Green Room", "ITS HAS A LOT OF PLANTS ", None, 'outside', 'road', 'side_door', 'outside_west', None,
                None)
road = Room('road', "long dirt road", None, 'South', None, None, 'SOUTH_HOUSE', None,  None)
SOUTH_HOUSE = Room('blue house', "looks old have wood walls and a fireplace", None, 'backroom', 'EAST_OF_LAKE', None,
                   'front_door', 'up_stair', None)
up_stair = Room("2 Floor", "it haves 3 room ", None, 'Hall''wide hall way', 'SOUTH_HOUSE', 'room1', 'BLUE_HOUSE', None,
                None)
room1 = Room('left_room', 'One bed and green walls', None, 'wall', 'wall', 'wall', 'up_stair', None, None)
BLUE_HOUSE = Room('2 Room', 'two beds', None, 'wall''window', 'wall', 'up_stair', 'EAST_OF_LAKE', None, None)
boat_1 = Room('boat_1', 'red', 'Armor', 'land_2', 'other boat', 'lake', None, None, None)
boat_2 = Room('boat_2', 'blue', None, 'land', 'underwater', 'EAST_OF_LAKE', 'dock',  None, None)
underwater = Room('uderwater' 'water', 'Axe', 'EAST_OF_LAKE', None, None, None, None, None, None)
land = Room('west land', 'has a lot of trees', 'Drug', 'Pruplehouse', 'yellow house', 'cave', 'a small house', None,
            None)
land_2 = Room('otherside', 'your on the other dock', None, 'tree', 'buncker', 'go back dock', 'Boat house', None, None)
pruplehouse = Room('pruplehouse', 'pruple', None, 'room1', 'room2', 'room3', 'room4', None, None)
cave = Room('cave', 'dark', 'Drink`', 'back of cave', None, None, None, None, None)
backofcave = Room('cave' 'dark', 'Chest', None, None, None, None, None, None, None)
yelow = Room('Yellow house', 'yellow', 'key', 'room1', 'room2', 'room3', 'room4', None, None)
small = Room('small house', 'very small', 'pickaxe', 'room1', 'Room2', 'Room3', 'Room4', None, None)
buncker = Room('little red house', 'E.H.S', 'tree', None, None, None, None, None, None)
TREE = Room('tree', 'its a tree', 'Vtec Just Kicked in Yo', None, None, None, None, None, None)
boathouse = Room('boat house', 'its haves boats but its lock', None, None, None, None, None, None, None,)
current_node = west_house
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']


class Item(object):
    def __init__(self, source, name, description, weight, material):
        self.power_source = source
        self.name = name
        self.description = description
        self.weight = weight
        self.material = material


class Knife(Item):
    def __init__(self, source, name, description, weight, material):
        super(Knife, self).__init__(source, name, description, weight, material)


class Weapon(Item):
    def __init__(self, source, name, description, weight, material):
        super(Weapon, self).__init__(source, name, description, weight, material)


class Inventory(Item):
    def __init__(self, source, name, description, weight, material):
        super(Inventory, self).__init__(source, name, description, weight, material)


class Drink(Item):
    def __init__(self, source, name, description, weight, material):
        super(Drink, self).__init__(source, name, description, weight, material)


class Armor(Item):
    def __init__(self, source, name, description, weight, material):
        super(Armor, self).__init__(source, name, description, weight, material)


class Axe(Item):
    def __init__(self, source, name, description, weight, material):
        super(Axe, self).__init__(source, name, description, weight, material)


class Key(Item):
    def __init__(self, source, name, description, weight, material):
        super(Key, self).__init__(source, name, description, weight, material)


class Chest(Item):
    def __init__(self, source, name, description, weight, material):
        super(Chest, self).__init__(source, name, description, weight, material)


class Drug(Item):
    def __init__(self, source, name, description, weight, material):
        super(Drug, self).__init__(source, name, description, weight, material)


class Backpack(Item):
    def __init__(self, source, name, description, weight, material):
        super(Backpack, self).__init__(source, name, description, weight, material)


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
