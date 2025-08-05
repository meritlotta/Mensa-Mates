import pygame
import sys

# colours
YELLOW = (248, 198, 98)
DARKVIOLET = (44, 38, 63)
LIGHTVIOLET = (89, 80, 130)

# fonts
pygame.font.init()
title_font = pygame.font.SysFont("verdana", 48)
small_font = pygame.font.SysFont("verdana", 24)
back_font = pygame.font.SysFont("verdana", 20)


def show_news(screen):
    # Sample fake news messages
    news_messages = [
        "NEW FEATURE: From now on, you get personalized meal recommendations!",
        "IMPROVED: Feedback section now supports one-line comments!",
        "COMING SOON: Mystery Meal Mode, spin the wheel and eat what fate decides!",
        "VEGAN-VISION: Now highlighting plant-based options with extra sparkle!",
        "SHARE & COMPARE: Find out who among your friends has the wildest taste!",

    ]

    clock = pygame.time.Clock()
    running = True

    back_button = pygame.Rect(50, 50, 105, 50)

    while running:
        screen.fill(LIGHTVIOLET)

        # Title
        title = title_font.render("News", True, YELLOW)
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 50))

        # Draw news boxes
        box_width = 1000
        box_height = 60
        start_x = 100
        start_y = 150
        spacing = 20

        for i, message in enumerate(news_messages):
            y = start_y + i * (box_height + spacing)
            box_rect = pygame.Rect(start_x, y, box_width, box_height)
            pygame.draw.rect(screen, DARKVIOLET, box_rect, border_radius=10)

            text = small_font.render(message, True, YELLOW)
            screen.blit(text, (start_x + 15, y + (box_height - text.get_height()) // 2))

        # Back button
        pygame.draw.rect(screen, (44, 38, 63), back_button, border_radius=70)
        back_text = back_font.render("<- Back", True, (248, 198, 98))
        back_text_rect = back_text.get_rect(center=back_button.center)
        screen.blit(back_text, back_text_rect)

        pygame.display.flip()

        # Exit on click or key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        pygame.display.flip()
        clock.tick(30)