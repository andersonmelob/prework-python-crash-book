favorite_numbers = {
    'anderson' : [7, 9],
    'tatyane' : [17, 10],
    'alysson' : [27, 8],
    'thais' : [37, 10],
    'isis' : [47, 11],
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite #'s are: ")
    for number in numbers:
        print("\t-", number)




