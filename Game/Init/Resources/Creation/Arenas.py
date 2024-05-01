import json
from ..Objects.Arena import Arena
# Judgement arena
with open('./Resources/Arenas/JudgementArena.json') as f:
    data = json.load(f)
JudgementArena = Arena(data['NAME'], data['WIDTH'], data['HEIGHT'], data['FLOOR_Y'])