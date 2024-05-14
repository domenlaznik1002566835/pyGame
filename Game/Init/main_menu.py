import pygame as pg

def main_menu(window):
    menu_font = pg.font.Font(None, 50)
    option_font = pg.font.Font(None, 35)
    title = menu_font.render("Main Menu", True, (255, 255, 255))

    options = [
        {"text": "Start", "action": lambda: start_game(window)},
        {"text": "Practice", "action": start_practice},
        {"text": "Settings", "action": open_settings},
        {"text": "Exit", "action": pg.quit}
    ]

    selected_option = 0

    running = True
    while running:
        window.fill((0, 0, 0))
        window.blit(title, (window.get_width() / 2 - title.get_width() / 2, window.get_height() / 2 - 100))

        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected_option else (100, 100, 100)
            text = option_font.render(option["text"], True, color)
            window.blit(text, (window.get_width() / 2 - text.get_width() / 2, window.get_height() / 2 + i * 50))

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                if event.key == pg.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                if event.key == pg.K_RETURN:
                    if options[selected_option]["text"] == "Start":
                        selected_characters = options[selected_option]["action"]()
                        return selected_characters
                        running = False
                        pg.quit()
                        quit()
                    else:
                        options[selected_option]["action"]()

def start_game(window):
    character_font = pg.font.Font(None, 35)
    characters = ["Hikaru", "Lucid", "Ronan"]
    selected_characters = []

    total_width = sum(character_font.size(character)[0] for character in characters)
    start_x = (window.get_width() - total_width) / 2

    selected_character = 0
    running = True
    while running:
        window.fill((0, 0, 0))

        x = start_x
        for i, character in enumerate(characters):
            if character in selected_characters:
                color = (212, 175, 55)
            elif i == selected_character:
                color = (255, 255, 255)
            else:
                color = (100, 100, 100)
            text = character_font.render(character, True, color)
            window.blit(text, (x, window.get_height() / 2))
            x += text.get_width() + 20

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key in [pg.K_LEFT]:
                    selected_character = (selected_character - 1) % len(characters)
                    while characters[selected_character] in selected_characters:
                        selected_character = (selected_character - 1) % len(characters)
                if event.key in [pg.K_RIGHT]:
                    selected_character = (selected_character + 1) % len(characters)
                    while characters[selected_character] in selected_characters:
                        selected_character = (selected_character + 1) % len(characters)
                if event.key == pg.K_RETURN and characters[selected_character] not in selected_characters:
                    selected_characters.append(characters[selected_character])
                    if len(selected_characters) == 2:
                        running = False

    return selected_characters

def start_practice():
    print("Starting practice mode...")

def open_settings():
    print("Opening settings...")