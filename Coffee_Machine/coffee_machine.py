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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def there_have_enough(current_ingredients):
    for item in current_ingredients:
        if current_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """This convert and exchange the old coins with new."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_successful(customer_money, drink_cost):
    if customer_money >= drink_cost:
        change = f"{customer_money - drink_cost:.2f}"
        print(f"Here is {change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_a_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


def prompt():
    # TODO Make an interactive input.
    return input('What would you like? (espresso/latte/cappuccino):')


while True:

    command = prompt()

    # TODO Make the machine go off.
    if command == "off":
        break

    # TODO Print report.
    if command == "report":
        print(f"Water:{resources['water']}")
        print(f"Milk:{resources['milk']}")
        print(f"Coffee:{resources['coffee']}")
        print(f"Money:{profit}")

    # TODO Check if resources is sufficient.
    else:
        drink = MENU[command]

        if there_have_enough(drink['ingredients']):

            # TODO Process the coins.
            payment = process_coins()

            # TODO Check if the transaction is successful or not.
            if is_successful(payment, drink['cost']):

                # TODO Make a coffee.
                make_a_coffee(command, drink['ingredients'])
