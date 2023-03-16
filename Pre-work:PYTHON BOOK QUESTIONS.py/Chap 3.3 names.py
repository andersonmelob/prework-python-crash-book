cars = ['lamborghini', 'ferrari', 'range over']
msg = 'My next car will be a {}.'
msg_2 = 'I will have a {} in a near future.'
msg_3 = 'I would love to also have a {}.'

print(msg.format(cars[0].title()))
print(msg_2.format(cars[1].upper()))
print(msg_3.format(cars[2].title()))