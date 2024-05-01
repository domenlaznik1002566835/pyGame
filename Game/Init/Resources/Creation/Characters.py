import json
from . import Weapons
from ..Objects.Character import Character

with open('./Resources/Characters/Lucid.json') as f:
    data = json.load(f)
Lucid = Character(data['NAME'], data['HEALTH'], data['SPEED'], data['JUMP_FORCE'], data['FALL_SPEED'], data['MAX_JUMP_COUNT'], data['WIDTH'], data['HEIGHT'])
Bucid = Character(data['NAME'], data['HEALTH'], data['SPEED'], data['JUMP_FORCE'], data['FALL_SPEED'], data['MAX_JUMP_COUNT'], data['WIDTH'], data['HEIGHT'])

Dagger = Weapons.Dagger
Lucid.add_weapon(Dagger)

Bagger = Weapons.Bagger
Bucid.add_weapon(Bagger)