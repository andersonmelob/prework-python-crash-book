cities = {
    'florida': {'country': 'usa', 'population': 22.25, 'fact': 'is the flattest state in america'},
    'ceara': {'country': 'brasil', 'population': 9.2, 'fact': 'is the largerst producers of cotton in brazil'},
    'bohemia':{'country': 'czech republic', 'population':6.9, 'fact': 'is well known by its cuisine'}
    }

for city, details in cities.items():
    print("\n", city.title()+ " is a state of "+ details['country'].title()+ " with a population of " + str(details['population'])+ "mills.")
    print("Fact: " + details['fact'] + ".")