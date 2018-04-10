class Room(object):
    def __init__(self, name, north):
        self.name = name
        self.north = north

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

WEST_HOUSE = Room('north', 'south', 'west', 'east')
home = Room()
SOUTH_HOUSE = Room('north', 'south', 'west', 'east')
room1 = Room()
BLUE_HOUSE = Room('north', 'south', 'west', 'east')
room2 = Room()
EAST_OF_LAKE = Room('north', 'south', 'west', 'east')
room3 = Room()
WEST_OF_HOME = Room('north', 'south', 'west', 'east')
current_node = home
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']



class Characters(object):
    def __init__(self, name, dialogue, description, action, health, death):
        self.name = name
        self.description = dialogue
        self.description = description
        self.action = action
        self.health = health
        self.death = death

    def death(self):
        self.death = True
        print("% died." % self.name)

    def damage(self, amount):
        self.health = amount
        if self.health <= 0:
            self.health = True


while True:
    print(current_node ['NAME'])  # change
    print(current_node['DESCRIPTION'])   # Change
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
      #  Change
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")