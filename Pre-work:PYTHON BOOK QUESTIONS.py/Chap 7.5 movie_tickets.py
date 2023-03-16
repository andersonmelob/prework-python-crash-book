tickets = '\nHow old are you? '
tickets += "\n(Type 'quit' to stop.)"

while True:
    age = input(tickets)

    if age == 'quit'.upper():
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 13:
            price = 10
        else:
            price = 15
        print(f" The tickets price is ${price}")
