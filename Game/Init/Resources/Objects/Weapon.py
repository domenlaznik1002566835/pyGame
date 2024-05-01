class Weapon:
    def __init__(self, name, damage, width, height, duel_wield=False):
        self.name = name
        self.damage = damage
        self.stage = -1
        self.rotation = 0
        self.width = width
        self.height = height
        self.duel_wield = duel_wield
        self.coordinates = []

    def set_coordinates(self, x, y):
        self.coordinates = [x, y]