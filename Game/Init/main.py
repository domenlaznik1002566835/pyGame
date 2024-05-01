# Imports
import pygame as pg
import numpy as np
import Resources.Creation.Arenas as Arenas
import Resources.Creation.Characters as Characters

pg.init()

# Judgement arena
current_arena = Arenas.JudgementArena
# Player 1
player1 = Characters.Lucid



window = pg.display.set_mode((current_arena.width, current_arena.height))
current_arena.draw(window)
player1.start(0 + current_arena.width/5, current_arena.height - current_arena.floor_y - player1.height)
player1.draw(window)

pg.display.update()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()