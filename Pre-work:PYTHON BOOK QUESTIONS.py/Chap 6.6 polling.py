favorite_languages = {
    'jen': 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

people = ['anderson', 'sarah', 'susane']

for person in people:
    if person in sorted(favorite_languages.keys()):
        print('\nHi ' + person.title() + ", thanks for taking the poll.")
    else:
        print('\n' + person.title() + ', please, take the poll.')