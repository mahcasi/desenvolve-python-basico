num_elementos1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {num_elementos1} elementos da lista 1:")
lista1 = []
for x in range(num_elementos1):
    lista1.append(int(input()))

num_elementos2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {num_elementos2} elementos da lista 2:")
lista2 = []
for x in range(num_elementos2):
    lista2.append(int(input()))



lista_intercalada = []
i, n = 0, 0


while i < num_elementos1 and n < num_elementos2:
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[n])
    i += 1
    n += 1


while i < num_elementos1:
    lista_intercalada.append(lista1[i])
    i += 1

while n < num_elementos2:
    lista_intercalada.append(lista2[n])
    n += 1


print("Lista intercalada:", end=" ")
for elemento in lista_intercalada:
    print(elemento, end=" ")
print()