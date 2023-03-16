persons = {
    'sonzera':{
    'first': 'anderson',
    'last': 'melo',
    'age': 35,
    'location':'coconut creek',
    },
    'soneca' : {
    'first' : 'alysson',
    'last' : 'melo',
    'age' : 27,
    'location' : 'fortaleza',
    }
}


for nick, person_info in persons.items():
    print("\nNick name: " + nick)
    full_name = person_info['first']+ ' ' + person_info['last']
    person_age = person_info['age']
    person_location = person_info['location']

    print("\tFull name: " + full_name.title())
    print("\tAge: " + str(person_age))
    print("\tLocation: " + person_location.title())



