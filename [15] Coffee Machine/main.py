MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "milk": 200,
    "coffee": 100,
}

total_money = 0

# DEFINITIONS
resources_depleted = False


# TODO: 4. Check resources sufficient?
def check_resources(coffee_type):
    global resources_depleted
    water_needed = MENU[coffee_type]['ingredients']['water']
    milk_needed = MENU[coffee_type]['ingredients']['milk']
    coffee_needed = MENU[coffee_type]['ingredients']['coffee']
    if resources['water'] >= water_needed:
        if resources['milk'] >= milk_needed:
            if resources['coffee'] >= coffee_needed:
                resources_depleted = False
            else:
                resources_depleted = True
                print("Sorry there is not enough coffee.")
        else:
            resources_depleted = True
            print("Sorry there is not enough milk.")
    else:
        resources_depleted = True
        print("Sorry there is not enough water.")


# TODO: 5. Process coins


def process_coins(coffee_type):
    global total_money
    global money_sufficient
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    money_given = quarters + dimes + nickles + pennies
    if money_given < MENU[coffee_type]['cost']:
        money_sufficient = False
    else:
        total_money += MENU[coffee_type]['cost']
    return money_given


money_sufficient = True


# TODO: 6. Check transactions successful.
def check_transaction(coffee_type, money_input):
    global money_sufficient
    if money_input > MENU[coffee_type]["cost"]:
        users_change = money_input - MENU[coffee_type]["cost"]
        money_sufficient = True
        return f"Here is your ${users_change:.2f} in change."
    else:
        money_sufficient = False
        return "Sorry that's not enough money. Money refunded."


# TODO: 7. Make Coffee
def make_coffee(coffee_type):
    # Reducing the resources.
    global resources
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    return f"Here is your {coffee_type}☕ Enjoy"


coffee_machine_on = True
while coffee_machine_on:
    # TODO: 1. Prompt user
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    # TODO: 3. Print report
    if user_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\nMoney: ${total_money:.2f}")
    elif user_choice != "off" and user_choice != "report":
        check_resources(user_choice)

        if not resources_depleted:
            users_money = process_coins(user_choice)
            print(check_transaction(user_choice, users_money))
            if money_sufficient:
                print(make_coffee(user_choice))
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
    else:
        coffee_machine_on = False
