frase = "Meu amor mora em Roma e me deu um ramo de flores"

espaço = 0
indices = []
for i in range(len(frase)): #intervalo do(tamanho da(frase)):
    if frase[i] in " ":
        espaço += 1
        indices.append(i)

print("Espaços em branco:" ,espaço)