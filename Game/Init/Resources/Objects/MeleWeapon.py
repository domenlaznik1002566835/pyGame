from .Weapon import Weapon

class MeleWeapon(Weapon):
    def __init__(self, name, damage, width, height, speed, duel_wield=False):
        super().__init__(name, damage, width, height, speed, duel_wield)
        self.swing_coordinates = []

    def set_swing_coordinates(self, coordinates):
        self.swing_coordinates = coordinates