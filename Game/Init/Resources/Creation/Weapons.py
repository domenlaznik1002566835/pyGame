import json
from ..Objects.MeleWeapon import MeleWeapon
from ..Objects.RangedWeapon import RangedWeapon

with open('./Resources/Weapons/Katana.json') as f:
    data = json.load(f)
Katana = MeleWeapon(data['NAME'], data['DAMAGE'], data['WIDTH'], data['HEIGHT'], data['SPEED'])
Katana.set_coordinates(5, -20)
katana_swing_coordinates = [[7, -20], [12, -20], [16, -20], [19, -20], [21, -20], [23, -20], [25, -20], [23, -20], [21, -20], [19, -20], [16, -20], [12, -20], [7, -20]]
Katana.set_use_coordinates(katana_swing_coordinates)
with open('./Resources/Weapons/Shiruken.json') as f:
    data = json.load(f)
Shiruken = RangedWeapon(data['NAME'], data['DAMAGE'], data['WIDTH'], data['HEIGHT'], data['SPEED'], data['COOLDOWN'])
Shiruken.set_coordinates(5, -20)

with open('./Resources/Weapons/Dagger.json') as f:
    data = json.load(f)
Dagger = MeleWeapon(data['NAME'], data['DAMAGE'], data['WIDTH'], data['HEIGHT'], data['SPEED'])
Dagger.set_coordinates(5, -20)
daggers_swing_coordinates = [[7, 2], [12, 4], [16, 6], [19, 6], [21, 4], [23, 0], [25, -6], [23, -12], [23, -14], [21, -16], [19, -18], [16, -20], [12, -22], [7, -24]]
Dagger.set_use_coordinates(daggers_swing_coordinates)
with open('./Resources/Weapons/ThrowingKnife.json') as f:
    data = json.load(f)
ThrowingKnife = RangedWeapon(data['NAME'], data['DAMAGE'], data['WIDTH'], data['HEIGHT'], data['SPEED'], data['COOLDOWN'])
ThrowingKnife.set_coordinates(5, -20)

with open('./Resources/Weapons/Sword.json') as f:
    data = json.load(f)
Sword = MeleWeapon(data['NAME'], data['DAMAGE'], data['WIDTH'], data['HEIGHT'], data['SPEED'])
Sword.set_coordinates(5, -30)
sword_swing_coordinates = [[7, -30], [12, -30], [16, -30], [19, -30], [21, -30], [23, -30], [25, -30], [23, -30], [21, -30], [19, -30], [16, -30], [12, -30], [7, -30]]
Sword.set_use_coordinates(sword_swing_coordinates)
with open('./Resources/Weapons/Rock.json') as f:
    data = json.load(f)
Rock = RangedWeapon(data['NAME'], data['DAMAGE'], data['WIDTH'], data['HEIGHT'], data['SPEED'], data['COOLDOWN'])
Rock.set_coordinates(5, -30)