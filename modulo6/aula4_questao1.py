pares = [x for x in range(20, 51) if x % 2 == 0]
print(f"Todos os números pares: {pares}")

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in valores]
print(f"O quadrado e todos os valores: {valores}")

div_7 = [x for x in range(1, 101) if x % 7 == 0]
print(f"Todos os números divisíveis por 7: {div_7}")

paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print(paridade)