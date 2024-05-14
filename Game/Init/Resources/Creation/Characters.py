import json
from . import Weapons
from ..Objects.Character import Character

with open('./Resources/Characters/Hikaru.json') as f:
    data = json.load(f)
Hikaru = Character(data['NAME'], data['HEALTH'], data['SPEED'], data['JUMP_FORCE'], data['FALL_SPEED'], data['MAX_JUMP_COUNT'], data['WIDTH'], data['HEIGHT'], data['SPRITE'])
Hikaru.add_weapon(Weapons.Katana)
Hikaru.add_weapon(Weapons.Shiruken)

with open('./Resources/Characters/Lucid.json') as f:
    data = json.load(f)
Lucid = Character(data['NAME'], data['HEALTH'], data['SPEED'], data['JUMP_FORCE'], data['FALL_SPEED'], data['MAX_JUMP_COUNT'], data['WIDTH'], data['HEIGHT'], data['SPRITE'])
Lucid.add_weapon(Weapons.Dagger)
Lucid.add_weapon(Weapons.ThrowingKnife)

with open('./Resources/Characters/Ronan.json') as f:
    data = json.load(f)
Ronan = Character(data['NAME'], data['HEALTH'], data['SPEED'], data['JUMP_FORCE'], data['FALL_SPEED'], data['MAX_JUMP_COUNT'], data['WIDTH'], data['HEIGHT'], data['SPRITE'])
Ronan.add_weapon(Weapons.Sword)
Ronan.add_weapon(Weapons.Rock)
