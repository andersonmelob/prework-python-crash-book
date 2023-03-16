sandwich_order = ['pastrami','chicken', 'pastrami', 'bacon and cheese', 'pastrami']
finished_sandwishes = []

print("Sorry guys, we ran out of Pastrami!")

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    sandwich = sandwich_order.pop()
    print(f'\nI made your {sandwich} sandwich.')

    finished_sandwishes.append(sandwich)

print(f"\n-=-=- Finished sandwishes -=-=-")
for sandwhish in finished_sandwishes:
    print(f'\nWe made a {sandwich} sandwich.')