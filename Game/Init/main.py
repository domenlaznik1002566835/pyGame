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
# Player 2
player2 = Characters.Bucid

pg.font.init()
font = pg.font.Font(None, 35)

window = pg.display.set_mode((current_arena.width, current_arena.height))
current_arena.draw(window)
player1.start(0 + current_arena.width/5, current_arena.height - current_arena.floor_y - player1.height, -1)
player1.draw(window)
player2.start(current_arena.width - current_arena.width/5, current_arena.height - current_arena.floor_y - player2.height, 1)
player2.draw(window)

pg.display.update()

running = True
while running:
    current_time = pg.time.get_ticks()
    keys = pg.key.get_pressed()
    # Player1
    if keys[pg.K_d]:
        player1.move('right', current_arena.width)
    if keys[pg.K_a]:
        player1.move('left', current_arena.width)
    if keys[pg.K_s]:
        if player1.previous_y < player1.y:
            player1.jump_multiplier = player1.fall_speed
    # Player2
    if keys[pg.K_RIGHT]:
        player2.move('right', current_arena.width)
    if keys[pg.K_LEFT]:
        player2.move('left', current_arena.width)
    if keys[pg.K_DOWN]:
        if player2.previous_y < player2.y:
            player2.jump_multiplier = player2.fall_speed

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            # Player1
            if event.key == pg.K_w:
                player1.jump()
            if event.key == pg.K_f:
                player1.current_weapon.stage = -1
                player1.use_weapon()
            # Player2
            if event.key == pg.K_UP:
                player2.jump()
            if event.key == pg.K_KP1:
                player2.current_weapon.stage = -1
                player2.use_weapon()
        if event.type == pg.KEYUP:
            # Player1
            if event.key == pg.K_s:
                player1.jump_multiplier = player1.jump_force
            # Player2
            if event.key == pg.K_DOWN:
                player2.jump_multiplier = player2.jump_force
        if event.type == pg.USEREVENT+1:
            # Player1
            if player1.using_weapon == True:
                if player1.current_weapon.stage < len(player1.current_weapon.swing_coordinates) - 1:
                    player1.current_weapon.stage += 1
                else:
                    player1.current_weapon.stage = -1
                    pg.time.set_timer(pg.USEREVENT + 1, 0)
                    player1.using_weapon = False
            # Player2
            if player2.using_weapon == True:
                if player2.current_weapon.stage < len(player2.current_weapon.swing_coordinates) - 1:
                    player2.current_weapon.stage += 1
                else:
                    player2.current_weapon.stage = -1
                    pg.time.set_timer(pg.USEREVENT + 1, 0)
                    player2.using_weapon = False

    # Player1
    if player1.jumping:
        player1.previous_y = player1.y
        player1.velocity -= (current_arena.gravity * player1.jump_multiplier)
        player1.y -= player1.velocity
        if player1.y >= current_arena.height - current_arena.floor_y - player1.height:
            player1.y = current_arena.height - current_arena.floor_y - player1.height
            player1.jumping = False
            player1.jump_count = 0
    # Player2
    if player2.jumping:
        player2.previous_y = player2.y
        player2.velocity -= (current_arena.gravity * player2.jump_multiplier)
        player2.y -= player2.velocity
        if player2.y >= current_arena.height - current_arena.floor_y - player2.height:
            player2.y = current_arena.height - current_arena.floor_y - player2.height
            player2.jumping = False
            player2.jump_count = 0

    if player1.current_weapon is not None and player1.current_weapon.get_hitbox().colliderect(player2.get_hitbox()) and player1.using_weapon == True:
        if current_time - player2.last_hit_time >= 500:
            player2.health -= player1.current_weapon.damage
            player2.last_hit_time = current_time
    if player2.current_weapon is not None and player2.current_weapon.get_hitbox().colliderect(player1.get_hitbox()) and player2.using_weapon == True:
        if current_time - player1.last_hit_time >= 500:
            player1.health -= player2.current_weapon.damage
            player1.last_hit_time = current_time

    window.fill((0, 0, 0))
    current_arena.draw(window)
    player1.draw(window)
    player2.draw(window)
    health_text1 = font.render(f"Player 1 Health: {player1.health}", True, (255, 255, 255))
    window.blit(health_text1, (300, 200))
    health_text2 = font.render(f"Player 2 Health: {player2.health}", True, (255, 255, 255))
    window.blit(health_text2, (window.get_width() - health_text2.get_width() - 300, 200))
    pg.display.update()

pg.quit()