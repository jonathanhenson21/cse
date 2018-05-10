class Item(object):
    def __init__(self, source, name, description, weight, material):
        self.power_source = source
        self.name = name
        self.description = description
        self.weight = weight
        self.material = material


class weapon(Item):
    def __init__(self, source, name, description, weight, material):
        super(weapon, self).__init__(source, name, description, weight, material)


class inventory(Item):
    def __init__(self, source, name, description, weight, material):
        super(inventory, self).__init__(source, name, description, weight, material)


class drink(Item):
    def __init__(self, source, name, description, weight, material):
        super(drink, self).__init__(source, name, description, weight, material)


class drink(Item):
    def __init__(self, source, name, description, weight, material):
        super(drink, self).__init__(source, name, description, weight, material)