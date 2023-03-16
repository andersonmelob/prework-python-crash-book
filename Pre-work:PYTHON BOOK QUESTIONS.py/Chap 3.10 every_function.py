countrys = ['brasil','eua','bahamas','mexico','russia']
countrys1 = []
countrys2 = []
countrys3 = [] 


for i in countrys:
    countrys1.append(i.title())
    countrys2.append(i.upper())
    countrys3.append(i.lower())
    
print(countrys1)
print()
print(countrys2)
print()
print(countrys3)
print()

countrys[2] = 'england'
print(countrys)

del countrys[-1]
print()
print(countrys)
print()
countrys.pop()
print(countrys)
print()
countrys.sort()
print(countrys)
countrys.sort(reverse=True)
print()
countrys.reverse()
print()
print(countrys)
print()
print(sorted(countrys))
print()
print(sorted(countrys, reverse=True))
print()
print(len(countrys))
print()
name = 'anderson melo'
print(len(name))