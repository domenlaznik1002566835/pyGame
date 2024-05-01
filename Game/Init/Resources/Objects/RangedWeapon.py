from .Weapon import Weapon

class RangedWeapon(Weapon):
    def __init__(self, name, damage, width, height, range, duel_wield=False):
        super().__init__(name, damage, width, height, duel_wield)
        self.range = range