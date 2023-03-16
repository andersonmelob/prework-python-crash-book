glossary = {
'boolean' : 'True or False',
'dictionary':'collection of key-value pairs',
'list' : 'mutable',
'tuple': 'imutable',
'variable':'holds a value'
}

for k, v in glossary.items():
    print('\n'+ k.title() + ': ' + v.title())