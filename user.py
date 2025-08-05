import pygame

def draw_profile_popup(screen, font, user_data):
    popup_rect = pygame.Rect(700, 120, 440, 130)
    pygame.draw.rect(screen, (44, 38, 63), popup_rect, border_radius=10)  # DARKVIOLET
    pygame.draw.rect(screen, (248, 198, 98), popup_rect, 4, border_radius=10)  # Yellow border

    # smaller font
    small_font = pygame.font.SysFont("verdana", 20)

    name_text = small_font.render(f"Name: {user_data['name']}", True, (248, 198, 98))
    email_text = small_font.render(f"Email: {user_data['email']}", True, (248, 198, 98))

    screen.blit(name_text, (popup_rect.x + 20, popup_rect.y + 30))
    screen.blit(email_text, (popup_rect.x + 20, popup_rect.y + 70))