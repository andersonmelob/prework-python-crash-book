favorite_places = {
    'anderson': ['california', 'prague'],
    'tatyane': ['lousiana', 'prague'],
    'alysson': ['rj'],
}

for name, places in favorite_places.items():
    print(f"{name.title()} loves: ")
    for place in places:
        print(f'\t{place.title()}')
