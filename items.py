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


class chest(Item):
    def __init__(self, source, name, description, weight, material):
        super(chest, self).__init__(source, name, description, weight, material)


class drug(Item):
    def __init__(self, source, name, description, weight, material):
        super(drug, self).__init__(source, name, description, weight, material)


class backpack(Item):
    def __init__(self, source, name, description, weight, material):
        super(backpack, self).__init__(source, name, description, weight, material)


class drink(Item):
    def __init__(self, source, name, description, weight, material):
        super(, self).__init__(source, name, description, weight, material)