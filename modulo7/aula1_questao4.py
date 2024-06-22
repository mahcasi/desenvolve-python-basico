numero = input("Digite o número: ")

if len(numero) == 8:
    numero_completo = '9' + numero
elif len(numero) == 9 and numero[0] == '9':
    numero_completo = numero

print(f"Número completo: {numero_completo[:5] + '-' + numero_completo[5:]}")