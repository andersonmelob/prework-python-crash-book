def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title, 'songs':songs}
    return album

print(make_album('Charlie Brown Jr.', 'Meu escritorio'))
print(make_album('Blink182', 'Blink 182', "I miss you"))
