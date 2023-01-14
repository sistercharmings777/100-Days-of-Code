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

# Program variables
cash = 0

# print(MENU['espresso']['ingredients']['water'])

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(user_drink):
    for item in resources:
        if resources[item] < user_drink[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins(price_of_drink):
    total = int(input("Insert quarters: ")) * 0.25
    total += int(input("Insert dimes: ")) * 0.10
    total += int(input("Inset nickles: ")) * 0.05
    total += int(input("Insert Pennies: ")) * 0.01
    if total < price_of_drink['cost']:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif total > price_of_drink['cost']:
        change = round(total - price_of_drink['cost'], 2)
        print(f"Here is ${change} dollars in change")
        global cash
        cash += price_of_drink['cost']
        return True


def coffee_maker(user_drink):
    for item in user_drink:
        resources[item] -= user_drink[item]
    print(f"Enjoy your drink")


is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${cash}")
    else:
        drink = MENU[user_choice]['ingredients']
        drink_price = MENU[user_choice]
        print(drink)
        enough_res = is_resource_sufficient(drink)
        if enough_res:
            payment = process_coins(drink_price)
            if payment:
                coffee_maker(drink)
