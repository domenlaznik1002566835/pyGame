import json
from ..Objects.MeleWeapon import MeleWeapon

with open('./Resources/Weapons/Dagger.json') as f:
    data = json.load(f)
Dagger = MeleWeapon(data['NAME'], data['DAMAGE'], data['WIDTH'], data['HEIGHT'], data['SPEED'], data['DUEL_WIELD'])
Dagger.set_coordinates(5, 0)
daggers_swing_coordinates = [[7, 2], [12, 4], [16, 6], [19, 6], [21, 4], [23, 0], [25, -6], [23, -12], [23, -14], [21, -16], [19, -18], [16, -20], [12, -22], [7, -24]]
Dagger.set_use_coordinates(daggers_swing_coordinates)

Bagger = MeleWeapon(data['NAME'], data['DAMAGE'], data['WIDTH'], data['HEIGHT'], data['SPEED'], data['DUEL_WIELD'])
Bagger.set_coordinates(5, 0)
Baggers_swing_coordinates = [[7, 2], [12, 4], [16, 6], [19, 6], [21, 4], [23, 0], [25, -6], [23, -12], [23, -14], [21, -16], [19, -18], [16, -20], [12, -22], [7, -24]]
Bagger.set_use_coordinates(daggers_swing_coordinates)