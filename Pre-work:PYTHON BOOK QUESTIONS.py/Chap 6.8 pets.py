pet_1 = {'animal': 'dog', 'owner':'anderson'}
pet_2 = {'animal': 'cat', 'owner':'karylane'}

pets = [pet_1, pet_2]

for pet in pets:
    print("\tThe pet is a " + pet['animal']+ ". And the owner is " + pet['owner'].title()+ ".")