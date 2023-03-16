glossary = {
'boolean' : 'True or False',
'dictionary':'collection of key-value pairs',
'list' : 'mutable',
'tuple': 'imutable',
'variable':'holds a value'
}

print("Glossary of words.\n")
print(f"Boolean: {glossary['boolean']}.")
print(f"Dictionary: {glossary['dictionary']}.") 
print(f"List: {glossary['list']}.")
print(f"Tuple: {glossary['tuple']}.")
print(f"Variable: {glossary['variable']}.")

'''for k, v in glossary.items():
    print("\nKey: " + k)
    print("Value: " + v)'''
    
'''for k in glossary:
    print(k)'''