import random

lista1, lista2 = [], []
for i in range(20):
    lista1.append(random.randint(0,50))
    lista2.append(random.randint(0,50))

print(lista1)
print(lista2)

inters = []
for elemento in lista1:
    if elemento in lista2 and elemento not in inters:
        inters.append(elemento)

inters.sort()
for i in inters:
    print (f"{i}: ({lista1.count(i)}, {lista2.count(i)})")
        