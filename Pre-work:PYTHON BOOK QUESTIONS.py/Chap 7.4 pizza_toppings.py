pizzas = 'which pizza topping would you like? '
pizzas += " (Type 'quit' to stop adding toppings!) "

while True:
    topping = input(pizzas)

    if topping == 'quit'.upper():
        break
    else:
        print(f"Adding {topping} to your pizza.")