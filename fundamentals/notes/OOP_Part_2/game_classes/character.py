class Character:
    #constructor
    def __init__(self):
        self.health = 100
        self. strength = 10
        self.level = 1
        self.defense = 5

    #attack method
    def attack(self, target):
        print("attacking")
        target.defend(self.strength)
        return self

    #defend method
    def defend(self, damage):
        actual_damage = damage - self.defense
        self.health -= actual_damage
