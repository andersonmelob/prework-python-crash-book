rivers = {
    'sao francisco' : 'brasil',
    'mississipi': 'usa',
    'nile' : 'egypt',
}

for river, country in rivers.items():
    print('\nRiver ' + river.title() + " runs through " + country.title() + ".")

    print('\nThe name of the rivers are:')
    print('\nRiver: ' + river.title())
    print()
    print('The name of the countrys that the rivers run through are: ')
    print(country)