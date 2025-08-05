import datetime

def get_today_menu():
    today = datetime.date.today().strftime("%A")

    if today == "Monday":
        return [
            "Pasta with red lentil Bolognese | 2,95€",
            "Bulgur and cabbage stew | 2,50€",
            "Small portion: Bulgur and cabbage stew | 1,45€",
            "Mediterranean-style soy strips, tomato-olive sauce, rice | 3,00€"
        ]
    elif today == "Tuesday":
        return [
            "Vegetable crispy schnitzel with brown sauce | 2,75€",
            "Bulgur and cabbage stew | 2,50€",
            "Alaska pollock fillet in ciabatta crust, basil sauce | 3,75€"
        ]
    elif today == "Wednesday":
        return [
            "Mediterranean bulgur | 2,95€",
            "Farfalle with lemon basil sauce and melted tomatoes | 3,00€",
            "Beef Bolognese with fusilli | 3, 60€"
        ]
    elif today == "Thursday":
        return [
            "Fried potato noodles with savoy cabbage | 2,95€",
            "Vegetable and jackfruit fish alternative, remoulade-style cream | 3,50€",
            "Potato wedges, garlic dip, salad | 2,75€"
        ]
    elif today == "Friday":
        return [
            "Pasta with spinach and feta-style cheese | 2,95€",
            "Curry sausage with spicy sauce | 3,75€"
        ]
    else:
        return ["The Mensa is closed today."]

