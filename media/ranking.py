import pygame
import sys

def show_ranking(screen, item, username):
    font = pygame.font.SysFont("verdana", 50)
    medium_font = pygame.font.SysFont("verdana", 35)
    small_font = pygame.font.SysFont("verdana", 20)
    clock = pygame.time.Clock()

    back_button = pygame.Rect(50, 50, 105, 50)

    # scale ranking
    ranking_value = None
    ranking_buttons = []
    button_size = 20
    spacing = 10
    ranking_y = 300

    total_width = 23 * button_size + 22 * spacing
    ranking_start_x = (screen.get_width() - total_width) // 2

    for i in range(23):
        x = ranking_start_x + i * (button_size + spacing)
        rect = pygame.Rect(x, ranking_y, button_size, button_size)
        ranking_buttons.append((rect, i))


    # textfield
    user_text = ""
    max_chars = 80
    active = False
    input_box = pygame.Rect(ranking_start_x, ranking_y + 100, total_width, 40)  # maybe smaller height for one line

    # save button
    save_button = pygame.Rect(ranking_start_x, input_box.bottom + 20, 150, 40)

    # saved message
    saved_message_timer = 0

    running = True
    while running:
        screen.fill((89, 80, 130))

        title = font.render("Ranking", True, (248, 198, 98))
        screen.blit(title, (500, 100))

        item_text = medium_font.render(f"{item}", True, (248, 198, 98))
        item_rect = item_text.get_rect(center=(screen.get_width() // 2, 190))
        screen.blit(item_text, item_rect)

        pygame.draw.rect(screen, (44, 38, 63), back_button, border_radius=70)
        back_text = small_font.render("<- Back", True, (248, 198, 98))
        screen.blit(back_text, (back_button.x + 10, back_button.y + 10))

        # ranking buttons
        for rect, value in ranking_buttons:
            color = (248, 198, 98) if ranking_value is not None and value <= ranking_value else (200, 180, 240)
            pygame.draw.rect(screen, color, rect, border_radius=70)
            label = small_font.render(str(value), True, (44, 38, 63))
            screen.blit(label, (rect.x, rect.y - 35))

        # text input
        box_color = (255, 255, 255) if active else (200, 200, 200)
        pygame.draw.rect(screen, box_color, input_box, border_radius=10)

        display_text = user_text
        text_surface = small_font.render(display_text, True, (44, 38, 63))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + (input_box.height - text_surface.get_height()) // 2))

        # character counter
        current_chars = len(user_text)
        counter_color = (255, 100, 100) if current_chars >= max_chars else (248, 198, 98)
        counter_text = small_font.render(f"{current_chars} / {max_chars}", True, counter_color)
        counter_x = input_box.x + input_box.width - counter_text.get_width() - 5
        counter_y = input_box.y + input_box.height + 5
        screen.blit(counter_text, (counter_x, counter_y))

        # feedback box
        instruction = small_font.render("More thoughts...?", True, (248, 198, 98))
        screen.blit(instruction, (input_box.x, input_box.y - 35))

        # save button
        pygame.draw.rect(screen, (44, 38, 63), save_button, border_radius=10)
        save_text = small_font.render("Save this", True, (248, 198, 98))
        screen.blit(save_text, (save_button.x + 10, save_button.y + 10))

        if saved_message_timer > 0:
            saved_text = small_font.render("SAVED!", True, (248, 198, 98))  # bright green for visibility
            screen.blit(saved_text, (save_button.x + save_button.width + 10, save_button.y + 10))
            saved_message_timer -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False

                elif save_button.collidepoint(event.pos):
                    with open("ranking.txt", "a", encoding="utf-8") as file:
                        file.write(f"Username: {username}\n")
                        file.write(f"Item: {item}\n")
                        file.write(f"Ranking: {ranking_value}\n")
                        file.write(f"Feedback: {user_text}\n")
                        file.write("-" * 40 + "\n\n")
                    saved_message_timer = 60

                elif input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                for rect, value in ranking_buttons:
                    if rect.collidepoint(event.pos):
                        ranking_value = value

            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    pass  # Do nothing (no new lines)
                elif len(user_text) < max_chars:
                    user_text += event.unicode

        pygame.display.flip()
        clock.tick(30)
