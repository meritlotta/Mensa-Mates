from helper import load_user_rankings
from menu import get_today_menu

def get_recommendation(username):
    rankings = load_user_rankings(username)
    today_menu = get_today_menu()

    # Filter out invalid rankings
    valid_rankings = [r for r in rankings if r.get("ranking") and r["ranking"].isdigit()]
    valid_rankings.sort(key=lambda x: int(x["ranking"]), reverse=True)

    # Find the highest-ranked item that is on today's menu
    for entry in valid_rankings:
        if entry["item"] in today_menu:
            return entry["item"]

    return "No recommended item available today."
