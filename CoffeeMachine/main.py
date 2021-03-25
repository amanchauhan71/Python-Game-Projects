from coffee_data import resources, MENU


def total_change(coffee_choice, total_cost):
    cost_value = float(coffee_choice["cost"])

    if total_cost > cost_value:
        return round(total_cost - cost_value, 2)
    else:

        return total_cost


def report_resources(ingredients_available):
    water = ingredients_available["water"]
    milk = ingredients_available["milk"]
    coffee = ingredients_available["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${ingredients_available['cost']}")


def check_enough_money(coffee_choice, pennies_coin):
    cost_value = float(coffee_choice["cost"])

    if pennies_coin >= cost_value:
        return True
    else:
        return False


def enough_resource(coffee_resource, choice_drink, choice_coffee):
    water = int(coffee_resource["water"])
    milk = int(coffee_resource["milk"])
    coffee = int(coffee_resource["coffee"])

    ingredients = choice_drink["ingredients"]
    ingredients_water = int(ingredients["water"])
    if choice_coffee != "espresso":
        ingredients_milk = int(ingredients["milk"])
    else:
        ingredients_milk = 0

    ingredients_coffee = int(ingredients["coffee"])

    if water < ingredients_water or milk < ingredients_milk or coffee < ingredients_coffee:
        return False
    else:
        return True


def update_report(report_cost_change, cost_update, choice_coffee):
    # print(report_cost_change)
    update_cost = float(report_cost_change["cost"])
    update_cost += float(cost_update["cost"])
    report_cost_change["cost"] = str(update_cost)

    ingredients = cost_update["ingredients"]
    ingredients_water = int(ingredients["water"])
    if choice_coffee != "espresso":
        ingredients_milk = int(ingredients["milk"])
    else:
        ingredients_milk = 0
    ingredients_coffee = int(ingredients["coffee"])

    update_water = int(report_cost_change["water"]) - ingredients_water
    if choice_coffee != "espresso":
        update_milk = int(report_cost_change["milk"]) - ingredients_milk
    else:
        update_milk = 0
    update_coffee = int(report_cost_change["coffee"]) - ingredients_coffee
    report_cost_change["water"] = str(update_water)

    if choice_coffee != "espresso":
        report_cost_change["milk"] = str(update_milk)

    report_cost_change["coffee"] = str(update_coffee)
    return report_cost_change


is_coffee_machine_available = True
resources.update({"cost": "0"})
while is_coffee_machine_available:
    choice = input(" What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "report":
        report_resources(resources)

    elif choice == "off":
        print("Machine is out of Maintenance")
        is_coffee_machine_available = False

    else:
        resource_available = enough_resource(resources, MENU[choice], choice)

        if not resource_available:
            print(" Sorry there is not enough water. ")
        else:
            print("Please insert coins.")
            coin_quarters = int(input("how many quarters?:"))
            coin_dimes = int(input("how many dimes?:"))
            coin_nickles = int(input("how many nickles?:"))
            coin_pennies = int(input("how many pennies?:"))

            pennies = coin_quarters * 0.25 + coin_dimes * 0.1 + coin_nickles * 0.05 + coin_pennies * 0.01
            cost_final = check_enough_money(MENU[choice], pennies)

            if cost_final:
                remaining_balance = total_change(MENU[choice], pennies)
                resources = update_report(resources, MENU[choice], choice)

                if cost_final != remaining_balance:
                    print(f"Here is ${remaining_balance} in change")
                print(f"Here is your {choice} ☕ Enjoy!")

            else:
                is_coffee_machine_available = False
                print("Sorry that's not enough money. Money refunded.")
