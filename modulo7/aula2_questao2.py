frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

# Substitui todas as ocorrências de vogais por "*"
frase_modificada = ""
for letra in frase:
    if letra in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += letra

print("Frase modificada:", frase_modificada)