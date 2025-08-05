import pygame
import sys
from helper import load_user_rankings

def load_user_rankings(username):
    with open("ranking.txt", "r", encoding="utf-8") as file:
        content = file.read().strip()

    blocks = content.split("-" * 40)
    rankings = []

    for block in blocks:
        lines = block.strip().split("\n")
        entry = {}
        for line in lines:
            if line.startswith("Username:"):
                entry["username"] = line.split(":", 1)[1].strip()
            elif line.startswith("Item:"):
                entry["item"] = line.split(":", 1)[1].strip()
            elif line.startswith("Ranking:"):
                entry["ranking"] = line.split(":", 1)[1].strip()
            elif line.startswith("Feedback:"):
                entry["feedback"] = line.split(":", 1)[1].strip()
        if entry.get("username") == username:
            rankings.append(entry)

    return rankings


def show_food_chart(screen, username):
    all_rankings = load_user_rankings(username)

    # Only keep entries with valid numeric rankings
    valid_rankings = [r for r in all_rankings if r.get("ranking") and r["ranking"].isdigit()]
    valid_rankings.sort(key=lambda x: int(x["ranking"]), reverse=True)

    font = pygame.font.SysFont("verdana", 35)
    small_font = pygame.font.SysFont("verdana", 20)
    clock = pygame.time.Clock()

    back_button = pygame.Rect(50, 50, 105, 50)
    next_button = pygame.Rect(1000, 720, 100, 40)
    prev_button = pygame.Rect(100, 720, 100, 40)

    items_per_page = 6
    current_page = 0

    running = True
    while running:
        screen.fill((89, 80, 130))

        title = font.render("Your Food Charts", True, (248, 198, 98))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 40))

        pygame.draw.rect(screen, (44, 38, 63), back_button, border_radius=70)
        back_text = small_font.render("<- Back", True, (248, 198, 98))
        screen.blit(back_text, (back_button.x + 10, back_button.y + 10))

        # Pagination logic
        start_index = current_page * items_per_page
        end_index = start_index + items_per_page
        page_rankings = valid_rankings[start_index:end_index]

        box_x = 100
        box_width = 1000
        y = 120
        entry_padding = 20

        for i, entry in enumerate(page_rankings):
            item = entry["item"]
            ranking = entry["ranking"]
            feedback = entry.get("feedback", "")

            lines = [f"{start_index + i + 1}. {item} – {ranking}/22"]
            if feedback:
                lines.append(f"Feedback: {feedback}")

            entry_height = 80 if feedback else 50
            entry_rect = pygame.Rect(box_x, y, box_width, entry_height)
            pygame.draw.rect(screen, (44, 38, 63), entry_rect, border_radius=10)

            text_y = y + 10
            for line in lines:
                color = (248, 198, 98) if "Feedback" not in line else (200, 180, 240)
                text_surface = small_font.render(line, True, color)
                screen.blit(text_surface, (box_x + 10, text_y))
                text_y += 25

            y += entry_height + entry_padding

        # Prev button
        if current_page > 0:
            pygame.draw.rect(screen, (44, 38, 63), prev_button, border_radius=70)
            prev_text = small_font.render("Previous", True, (248, 198, 98))
            prev_text_rect = prev_text.get_rect(center=prev_button.center)
            screen.blit(prev_text, prev_text_rect)

        # Next button
        if end_index < len(valid_rankings):
            pygame.draw.rect(screen, (44, 38, 63), next_button, border_radius=70)
            next_text = small_font.render("Next", True, (248, 198, 98))
            next_text_rect = next_text.get_rect(center=next_button.center)
            screen.blit(next_text, next_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False
                elif next_button.collidepoint(event.pos) and end_index < len(valid_rankings):
                    current_page += 1
                elif prev_button.collidepoint(event.pos) and current_page > 0:
                    current_page -= 1

        pygame.display.flip()
        clock.tick(30)
