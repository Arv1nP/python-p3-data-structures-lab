spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] >= 5]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return {
                'name': food['name'],
                'cuisine': food['cuisine'],
                'heat_level': food['heat_level']
            }
    # Return None if no matching food is found
    return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] >= 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
    return None


def get_average_heat_level(spicy_foods):
    total_heat = 0

    for food in spicy_foods:
        total_heat += food['heat_level']

    average = total_heat / len(spicy_foods) 
    return average


def create_spicy_food(spicy_foods, spicy_food):
    old_version = spicy_foods.copy()
    old_version.append(spicy_food)
    return old_version
