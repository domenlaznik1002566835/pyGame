# Imports
import pygame as pg
import numpy as np
import Resources.Creation.Arenas as Arenas
import Resources.Creation.Characters as Characters
from Resources.Objects.MeleWeapon import MeleWeapon
from Resources.Objects.RangedWeapon import RangedWeapon
from main_menu import main_menu

pg.init()

# Judgement arena
current_arena = Arenas.JudgementArena

window = pg.display.set_mode((current_arena.width, current_arena.height))
result = main_menu(window)

if len(result) == 2:
    if(result[0] == 'Hikaru'):
        player1 = Characters.Hikaru
    elif(result[0] == 'Lucid'):
        player1 = Characters.Lucid
    elif(result[0] == 'Ronan'):
        player1 = Characters.Ronan
    if(result[1] == 'Hikaru'):
        player2 = Characters.Hikaru
    elif(result[1] == 'Lucid'):
        player2 = Characters.Lucid
    elif(result[1] == 'Ronan'):
        player2 = Characters.Ronan


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
                player1.current_weapon = player1.weapons[0]
                player1.current_weapon.stage = -1
                player1.use_weapon()
            if event.key == pg.K_g:
                player1.current_weapon = player1.weapons[1]
                player1.use_weapon()
            # Player2
            if event.key == pg.K_UP:
                player2.jump()
            if event.key == pg.K_KP1:
                player2.current_weapon = player2.weapons[0]
                player2.current_weapon.stage = -1
                player2.use_weapon()
            if event.key == pg.K_KP2:
                player2.current_weapon = player2.weapons[1]
                player2.use_weapon()
        if event.type == pg.KEYUP:
            # Player1
            if event.key == pg.K_s:
                player1.jump_multiplier = player1.jump_force
            # Player2
            if event.key == pg.K_DOWN:
                player2.jump_multiplier = player2.jump_force
        if event.type == pg.USEREVENT + 1:
            # Player1
            if player1.using_weapon == True:
                if isinstance(player1.current_weapon, MeleWeapon) and player1.current_weapon.stage < len(
                        player1.current_weapon.swing_coordinates) - 1:
                    player1.current_weapon.stage += 1
                else:
                    player1.current_weapon.stage = -1
                    pg.time.set_timer(pg.USEREVENT + 1, 0)
                    player1.using_weapon = False
            # Player2
            if player2.using_weapon == True:
                if isinstance(player2.current_weapon, MeleWeapon) and player2.current_weapon.stage < len(
                        player2.current_weapon.swing_coordinates) - 1:
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

    if player1.current_weapon is player1.weapons[0] and player1.current_weapon.get_hitbox().colliderect(player2.get_hitbox()) and player1.using_weapon == True:
        if current_time - player2.last_hit_time >= 500:
            player2.health -= player1.current_weapon.damage
            player2.last_hit_time = current_time
    if player2.current_weapon is player2.weapons[0] and player2.current_weapon.get_hitbox().colliderect(player1.get_hitbox()) and player2.using_weapon == True:
        if current_time - player1.last_hit_time >= 500:
            player1.health -= player2.current_weapon.damage
            player1.last_hit_time = current_time
    for projectile in player1.weapons[1].projectiles:
        if projectile.get_hitbox().colliderect(player2.get_hitbox()):
            player2.health -= player1.weapons[1].damage
            player1.weapons[1].projectiles.remove(projectile)
    for projectile in player2.weapons[1].projectiles:
        if projectile.get_hitbox().colliderect(player1.get_hitbox()):
            player1.health -= player2.weapons[1].damage
            player2.weapons[1].projectiles.remove(projectile)

    window.fill((0, 0, 0))
    current_arena.draw(window)
    player1.draw(window)
    player2.draw(window)
    health_text1 = font.render(f"{player1.name} Health: {player1.health}", True, (255, 255, 255))
    window.blit(health_text1, (300, 200))
    health_text2 = font.render(f"{player2.name} Health: {player2.health}", True, (255, 255, 255))
    window.blit(health_text2, (window.get_width() - health_text2.get_width() - 300, 200))
    if player1.weapons[1].projectiles != []:
        player1.weapons[1].draw_projectiles(window, current_arena.width)
    if player2.weapons[1].projectiles != []:
        player2.weapons[1].draw_projectiles(window, current_arena.width)
    pg.display.update()

pg.quit()