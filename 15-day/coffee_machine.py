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
    "milk": 200,
    "coffee": 100,
}

money = 0


def report(resources, money):
    return f" Water: {resources['water']}ml\n Milk:{resources['milk']}ml\n Coffee: {resources['coffee']}g\n Money:${money}"


def update_resource(resources, menu):
    if menu.get('water'):
        resources['water'] = resources['water'] - menu['water']
    if menu.get('milk'):
        resources['milk'] = resources['milk'] - menu['milk']
    if menu.get('coffee'):
        resources['coffee'] = resources['coffee'] - menu['coffee']


is_true = True


def compare(resources, menu):
    if menu.get('water'):
        if resources['water'] < menu['water']:
            return "water"
    if menu.get('milk'):
        if resources['milk'] < menu['milk']:
            return "milk"
    if menu.get('coffee'):
        if resources['coffee'] < menu['coffee']:
            return "coffee"
    return 1


while is_true:
    choice_user = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice_user == 'report':
        print(report(resources, money))
    elif choice_user == 'off':
        is_true = False
    else:
        ch = compare(resources, MENU[choice_user]['ingredients'])
        if ch == 1:
            print("Please insert coins.")
            quarter = 0.25
            dime = 0.10
            nickle = 0.05
            pennie = 0.01
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total = (quarter * quarters) + (dime * dimes) + (nickle * nickles) + (pennie * pennies)
            if (MENU[choice_user]['cost']) <= total:
                amount_balance = round(total - (MENU[choice_user]['cost']), 2)
                money += MENU[choice_user]['cost']
                print(f"Here is ${amount_balance} in change.")
                print(f"Here is your {choice_user} ☕️. Enjoy!")
                update_resource(resources, MENU[choice_user]['ingredients'])
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {ch}.")
            is_true = True




