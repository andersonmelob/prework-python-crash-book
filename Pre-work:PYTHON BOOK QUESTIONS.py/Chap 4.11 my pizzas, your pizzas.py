pizzas = ['4 queijos', 'Carne a moda', 'frango catupiri', 'bacon']
friend_pizzas = pizzas[:]
for pizza in pizzas:
    print('I will get a ' + pizza.title() +', but I like perpperoni.\n')
print('I really love pizza!\n')
pizzas.append('perperoni')
print()
print(pizzas)
friend_pizzas.append('chocolate')
print(friend_pizzas)
print()
print('My favorite pizzas are: ')
for my_favorie in pizzas:
    print(my_favorie)
print()
print("My friend's favoite pizzas are: ")
for friend in friend_pizzas:
    print(friend)
print()




