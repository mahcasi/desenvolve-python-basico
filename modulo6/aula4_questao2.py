frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
espaçamento = " "

lista_vogais = sorted([letra for letra in frase if letra in vogais])
lista_consoantes = [letra for letra in frase if letra not in vogais and letra not in espaçamento]

print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)