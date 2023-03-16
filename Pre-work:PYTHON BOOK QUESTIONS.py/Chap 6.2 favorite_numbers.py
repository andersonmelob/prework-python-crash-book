favorite_numbers = {
    'anderson' : 7,
    'tatyane' : 17,
    'alysson' : 27,
    'thais' : 37,
    'isis' : 47,
}

'''print(f"Anderson favorite number is {favorite_numbers['anderson']}.\n")
print(f"Tatyane favorite number is {favorite_numbers['tatyane']}.\n")
print(f"Alysson favorite number is {favorite_numbers['alysson']}.\n")
print(f"Thais favorite number is {favorite_numbers['thais']}.\n")
print(f"Isis favorite number is {favorite_numbers['isis']}.\n")'''

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite # is: " + str(numbers))