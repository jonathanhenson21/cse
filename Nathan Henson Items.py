class Item(object):
    def __init__(self, source, name, description, weight, material):
        self.power_source = source
        self.name = name
        self.description = description
        self.weight = weight
        self.material = material


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


class drink(Item):
    def __init__(self, source, name, description, weight, material):
        super(drink, self).__init__(source, name, description, weight, material)

class axe(Item):
    def __init__(self, source, name, description, weight, material):
        super(axe, self).__init__(source, name, description, weight, material)

class Key(Item):
    def __init__(self, source, name, description, weight, material):
        super(Key, self).__init__(source, name, description, weight, material)


class Chest(Item):
    def __init__(self, source, name, description, weight, material):
        super(Chest, self).__init__(source, name, description, weight, material)


class Drug(Item):
    def __init__(self, source, name, description, weight, material):
        super(Drug, self).__init__(source, name, description, weight, material)


class Back_pack(Item):
    def __init__(self, source, name, description, weight, material):
        super(Back_pack, self).__init__(source, name, description, weight, material)


class Skatebord(Item):
    def __init__(self, source, name, description, weight, material):
        super(Skatebord, self).__init__(source, name, description, weight, material)
