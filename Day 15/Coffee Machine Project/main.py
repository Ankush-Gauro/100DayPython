MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

machine_on = True
money = 0
coffee_category = ['espresso','latte', 'cappuccino']

def generate_report():
    for i in resources:
        print(f"{i} : {resources[i]}")
    print(f"Money : {money}")

def check_resources(coffee_type):
    for item in MENU[coffee_type]['ingredients']:
        if  MENU[coffee_type]['ingredients'][item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True

def process_coins(coffee_type):
    global money
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total_money = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

    if total_money > MENU[coffee_type]['cost']:
        change = round(total_money - MENU[coffee_type]['cost'], 2)
        print(f"Here is {change} dollars in change.")
        money += MENU[coffee_type]['cost']
        return True
    elif total_money == MENU[coffee_type]['cost']:
        money += MENU[coffee_type]['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_type):
    resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
    resources['water'] -= MENU[coffee_type]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
    print(f"Here is your {coffee_type}. Enjoy!")


while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'off':
        machine_on = False
    elif user_input == 'report':
        generate_report()

    elif user_input in coffee_category:
        if check_resources(user_input):
            if process_coins(user_input):
                make_coffee(user_input)
            else:
                machine_on = False
        else:
            machine_on = False