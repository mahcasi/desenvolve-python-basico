numeros = []

print("Digite uma sequência de pelo menos 4 números inteiros (digite 0 para encerrar):")
while numeros != 0:
    num = int(input("Digite um número (ou 0 para encerrar): "))
    if num == 0 and len(numeros) >= 4:
        break
    else:
        numeros.append(num)

print("Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[1::2])
print("Elementos de índice ímpar:", numeros[::2])