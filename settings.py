import pygame
import sys

def show_settings(screen):
    font = pygame.font.SysFont("verdana", 50)
    small_font = pygame.font.SysFont("verdana", 20)
    clock = pygame.time.Clock()

    back_button = pygame.Rect(50, 50, 105, 50)

    # ON/OFF values as strings
    setting1_value = "ON"
    setting2_value = "OFF"
    setting3_value = "ON"

    # create rects for background rectangles behind text
    rect1 = pygame.Rect(190, 245, 800, 38)
    rect2 = pygame.Rect(190, 295, 800, 38)
    rect3 = pygame.Rect(190, 345, 800, 38)

    running = True
    while running:
        screen.fill((89, 80, 130))

        title = font.render("Settings", True, (248, 198, 98))
        screen.blit(title, (500, 100))

        # pretend settings
        setting1 = small_font.render("Dark mode: ", True, (248, 198, 98))
        setting2 = small_font.render("Notifications: ", True, (248, 198, 98))
        setting3 = small_font.render("Private Account: ", True, (248, 198, 98))

        # draw green rectangles behind text
        pygame.draw.rect(screen, (44, 38, 63), rect1, border_radius=10)
        pygame.draw.rect(screen, (44, 38, 63), rect2, border_radius=10)
        pygame.draw.rect(screen, (44, 38, 63), rect3, border_radius=10)

        # draw text on top
        screen.blit(setting1, (200, 250))
        screen.blit(setting2, (200, 300))
        screen.blit(setting3, (200, 350))

        # draw ON/OFF values next to setting text
        value1 = small_font.render(setting1_value, True, (248, 198, 98))
        value2 = small_font.render(setting2_value, True, (248, 198, 98))
        value3 = small_font.render(setting3_value, True, (248, 198, 98))

        screen.blit(value1, (750, 250))
        screen.blit(value2, (750, 300))
        screen.blit(value3, (750, 350))


        # Back button
        pygame.draw.rect(screen, (44, 38, 63), back_button, border_radius=70)
        back_text = small_font.render("<- Back", True, (248, 198, 98))
        screen.blit(back_text, (back_button.x + 10, back_button.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False
                elif rect1.collidepoint(event.pos):
                    setting1_value = "OFF" if setting1_value == "ON" else "ON"
                elif rect2.collidepoint(event.pos):
                    setting2_value = "OFF" if setting2_value == "ON" else "ON"
                elif rect3.collidepoint(event.pos):
                    setting3_value = "OFF" if setting3_value == "ON" else "ON"


        pygame.display.flip()
        clock.tick(30)
