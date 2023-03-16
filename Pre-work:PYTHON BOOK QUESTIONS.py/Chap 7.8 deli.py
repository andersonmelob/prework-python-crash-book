sandwich_order = ['pastrami','chicken', 'misto', 'bacon and cheese', 'pastrami']
finished_sandwishes = []

while sandwich_order:
    sandwich = sandwich_order.pop()
    print(f'\nI made your {sandwich} sandwish.')

    finished_sandwishes.append(sandwich)
print(f"\n-=-=- Finished sandwishes -=-=-")
for sandwhish in finished_sandwishes:
    print(f'\nWe made a {sandwhish} sandwish.')