# TODO: 1. Data
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

# TODO: 2. Resources_check

current_resources = resources


# TODO: 3. Currency

coins_operated = dict(Quarter=.25, Nickel=.05, Dime=.1, Penny=.01)


def money(q, n, d, p, item):
    total_money = q+n+d+p
    if MENU[item]["cost"] > total_money:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = total_money-MENU[item]["cost"]
        print(f"Here is ${change} in change.")
        return True


def check_resources(item):
    global current_resources
    for i in MENU[item]["ingredients"]:
        if current_resources[i] < MENU[item]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
        else:
            return True


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print(current_resources)
    else:
        if check_resources(order) :
            if money(int(input("Please insert coins.\nhow many quarters?:")),
                                            int(input("how many Dimes?:")),
                                            int(input("how many Nickles?:")),
                                            int(input("how many Pennies?:")), order):
                print(f"Here is your {order} ☕️. Enjoy!")
                for i in MENU[order]["ingredients"]:
                    current_resources[i] = current_resources[i]-MENU[order]["ingredients"][i]
            else:
                break








