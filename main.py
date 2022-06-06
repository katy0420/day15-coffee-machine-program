MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 500,
    "coffee": 100,
}


# TODO: 4. Check resources sufficient?
def resources_sufficient(order_menu):
    for item in order_menu:
        if order_menu[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 5. Process coins.
def process_coin():
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    user_input = quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
    return user_input


def update_resources(order_menu):
    for item in order_menu:
        resources[item] = resources[item] - order_menu[item]


profit = 0.0
power_on = True
while power_on:
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    choice = input("What would you like? (espresso/latte/cappuccino):")

    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if choice == "off":
        power_on = False

    # TODO: 3. Print report
    elif choice == "report":
        print("Water: " + str(resources.get("water")) + "ml")
        print(f"Milk: {resources['milk']}ml")
        print("Coffee: " + str(resources.get("coffee")) + "g")
        print("Money: $" + str(profit))
    else:
        drink = MENU[choice]
        cost = drink.get("cost")
        if resources_sufficient(drink.get("ingredients")):
            print("Please insert coins.")
            # TODO: 6. Check transaction successful
            coins = process_coin()
            if coins < cost:
                print("Sorry that's not enough money. Money refunded.")
                continue

            if coins > cost:
                change = round(coins-cost, 2)
                print(f"Here is ${change} dollars in change.")
            profit += cost

            # TODO: 7. Make Coffee.
            update_resources(drink.get("ingredients"))
            print(f"Here is your {choice} ☕️. Enjoy!")
