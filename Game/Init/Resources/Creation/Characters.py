import json
from ..Objects.Character import Character

with open('./Resources/Characters/Lucid.json') as f:
    data = json.load(f)
Lucid = Character(data['NAME'], data['HEALTH'], data['SPEED'], data['JUMP_FORCE'], data['FALL_SPEED'], data['WIDTH'], data['HEIGHT'])