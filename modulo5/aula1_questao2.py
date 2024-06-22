import random
import math

n = int(input("Digite a quantidade de valores: "))
soma = 0

for i in range (n):
    valor = random.randint(0,100)
    print(valor)
    soma += valor
    # soma  += random.randint(0,100)

print(f"A soma dos valores é {soma}")
print(f"A raiz quadrada da soma é {math.sqrt(soma):.2f}")