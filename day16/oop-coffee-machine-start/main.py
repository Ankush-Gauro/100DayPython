from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
my_money = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while machine_on:
    user_choice = input("“What would you like? (espresso/latte/cappuccino/): ").lower()
    if user_choice == 'off':
        machine_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        my_money.report()
    elif user_choice in ('espresso', 'latte', 'cappuccino'):
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if my_money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                print("Sorry, order can't be processed.")
        else:
            print("Sorry, there is not enough resource.")
            machine_on = False

