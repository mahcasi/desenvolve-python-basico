frase = "Meu amor mora em Roma e me deu um ramo de flores"

count_vogais = 0
indices = []
for i in range(len(frase)): #intervalo do(tamanho da(frase)):
    if frase[i] in "aeiou":
        count_vogais += 1
        indices.append(i)

print(count_vogais, "vogais")
print("Índices", indices)