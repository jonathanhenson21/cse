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


Johnny_Ghost = (140, False)
