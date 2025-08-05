import pygame
import sys
from user import draw_profile_popup
from menu import get_today_menu
from settings import show_settings
from ranking import show_ranking
from foodcharts import show_food_chart
from recommendation import get_recommendation
from news import show_news

pygame.init()

# Fonts
font = pygame.font.SysFont("verdana", 50, bold=True)
menu_font = pygame.font.SysFont("verdana", 36)
medium_font = pygame.font.SysFont("verdana", 32)
small_font = pygame.font.SysFont("verdana", 24)
small_font_italic = pygame.font.SysFont("verdana", 20, italic=True)


def get_user_name(screen):
    font = pygame.font.SysFont("verdana", 36)
    input_active = True
    user_input = ""
    clock = pygame.time.Clock()

    while input_active:
        screen.fill((44, 38, 63))


        prompt = font.render("Please enter your first and last name:", True, (248, 198, 98))
        screen.blit(prompt, (200, 270))

        input_box = pygame.Rect(200, 320, 800, 50)
        pygame.draw.rect(screen, (248, 198, 98), input_box, 2)

        input_text = font.render(user_input, True, (248, 198, 98))
        screen.blit(input_text, (input_box.x + 10, input_box.y + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        pygame.display.flip()
        clock.tick(30)

    return user_input

# Colour scheme
YELLOW = (248, 198, 98)
LIGHTVIOLET = (89, 80, 130)
DARKVIOLET = (44, 38, 63)
LIGHTGREEN = (65, 100, 74)
DARKGREEN = (50, 60, 50)

# Screen setup
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = LIGHTVIOLET
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mensa Mates")

# Ask user for name
user_full_name = get_user_name(screen)

# Split into first and last name
user_first_name = user_full_name.split()[0]
user_last_name = user_full_name.split()[1]

# user info
user_data = {
    "name": user_full_name,
    "email": f"{user_first_name}.{user_last_name}@stud.leuphana.de".lower()
}

# user image
user_image = pygame.image.load("media/user.PNG")
user_image = pygame.transform.smoothscale(user_image, (80, 80))
user_rect = user_image.get_rect(topleft=(1050, 30))

setting_image = pygame.image.load("media/settings.png")
setting_image = pygame.transform.smoothscale(setting_image, (80, 80))
setting_rect = setting_image.get_rect(topleft=(1050, 150))

profile_open = False

# chart image
chart_image = pygame.image.load("media/charts.PNG")
chart_image = pygame.transform.smoothscale(chart_image, (80, 80))
chart_rect = chart_image.get_rect(topleft=(1050, 270))

# notifications image
news_image = pygame.image.load("media/news.PNG")
news_image = pygame.transform.smoothscale(news_image, (80, 80))
news_rect = news_image.get_rect(topleft=(1050, 390))

def draw_header(screen, text, font, color, y=10):
    header = font.render(text, True, color)
    header_rect = header.get_rect(center=(screen.get_width() // 2, y + header.get_height() // 2))
    screen.blit(header, header_rect)

def draw_menutext(screen, text, font, color, x, y):
    menutext = font.render(text, True, color)
    screen.blit(menutext, (x, y))

# main loop
while True:
    screen.fill(BACKGROUND_COLOR)

    # Header
    draw_header(screen, "Mensa Mates", font, YELLOW, y=50)

    # Menu
    draw_menutext(screen, "Todays menu:", menu_font, YELLOW, x=100, y=170)

    subtitle = small_font_italic.render("Click on what you ate today", True, YELLOW)
    screen.blit(subtitle, (100, 215))

    # Recommendations
    recommended_item = get_recommendation(user_full_name)

    rec_line1 = medium_font.render("Based on previous rankings I recommend today:", True, YELLOW)
    screen.blit(rec_line1, (100, 525))

    rec_line2 = small_font.render(recommended_item, True, YELLOW)

    # Draw purple rectangle same size as menu boxes
    rec_box_x = 100
    rec_box_y = 580  # slightly higher than your previous 580 to match layout
    box_width = 900
    box_height = 55

    pygame.draw.rect(screen, DARKVIOLET, (rec_box_x, rec_box_y, box_width, box_height), border_radius=10)

    # Center the text vertically in the box
    text_y = rec_box_y + (box_height - rec_line2.get_height()) // 2
    screen.blit(rec_line2, (rec_box_x + 10, text_y))

    # Clickable menu boxes
    menu_items = get_today_menu()
    box_width =  900
    box_height = 55
    line_height = box_height + 10
    box_x = 100
    start_y = 250

    clickable_rects = []

    for i, item in enumerate(menu_items):
        box_y = start_y + i * line_height

        item_rect = pygame.Rect(box_x, box_y, box_width, box_height)
        pygame.draw.rect(screen, DARKVIOLET, item_rect, border_radius=10)

        item_text = small_font.render(item, True, YELLOW)
        text_y = box_y + (box_height - item_text.get_height()) // 2
        screen.blit(item_text, (box_x + 10, text_y))

        clickable_rects.append((item_rect, item))


    # Draw user image
    screen.blit(user_image, user_rect)

    # Draw Setting image
    screen.blit(setting_image, setting_rect)

    # Draw Charts image
    screen.blit(chart_image, chart_rect)

    # Draw Notifications image
    screen.blit(news_image, news_rect)

    # Show popup if open
    if profile_open:
        draw_profile_popup(screen, font, user_data)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if user_rect.collidepoint(event.pos):
                profile_open = not profile_open

            elif setting_rect.collidepoint(event.pos):
                show_settings(screen)

            elif chart_rect.collidepoint(event.pos):
                show_food_chart(screen, user_full_name)

            elif news_rect.collidepoint(event.pos):
                show_news(screen)

            for rect, item in clickable_rects:
                if rect.collidepoint(event.pos):
                    show_ranking(screen, item, user_full_name)

    pygame.display.flip()
