import json

from Game.Init.Resources.Objects.Arena import Arena
from Game.Init.Resources.Objects.DragonArena import DragonArena

with open('./Resources/Arenas/DragonArena.json') as f:
    data = json.load(f)
DragonArenaInstance = DragonArena(data['NAME'], data['WIDTH'], data['HEIGHT'], data['GRAVITY'], data['FLOOR_Y'])
DragonArenaInstance.load_platforms()

with open('./Resources/Arenas/JudgementArena.json') as f:
    data = json.load(f)
JudgementArena = Arena(data['NAME'], data['WIDTH'], data['HEIGHT'], data['GRAVITY'], data['FLOOR_Y'])
