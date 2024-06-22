import random

aleatorios = []
for i in range(20):
    valor = random.randint(-100, 100)
    aleatorios.append(valor)


print(sorted(aleatorios))
print(aleatorios)
print("O maior maior está no indice: ", aleatorios.index(max(aleatorios)))
print("O maior menor está no indice: ", aleatorios.index(min(aleatorios)))