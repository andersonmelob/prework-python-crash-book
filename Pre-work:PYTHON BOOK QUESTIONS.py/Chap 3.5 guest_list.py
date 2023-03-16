guest_list = ['Maize','Chico Melo','Taty']
msg = 'I would love to invite you, {}, for dinner with me.'

print(msg.format(guest_list[0]))
print(msg.format(guest_list[1]))
print(msg.format(guest_list[2]))
print()
print('Unfortunately, just found out that {} can not make it.'.format(guest_list[0]))
print()
guest_list[0] = 'Isis'
print(guest_list)
print()
print(msg.format(guest_list[0]))
print(msg.format(guest_list[1]))
print(msg.format(guest_list[2]))
