import os

# Ler o conteúdo do arquivo "frase.txt"
with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()

# Filtrar apenas caracteres alfabéticos e espaços
conteudo_filtrado = ''.join([caractere if caractere.isalpha() or caractere.isspace() else '' for caractere in conteudo])

# Dividir o conteúdo em palavras
palavras = conteudo_filtrado.split()

# Salvar as palavras em "palavras.txt", cada uma em uma linha
with open("palavras.txt", "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Ler e imprimir o conteúdo do arquivo "palavras.txt"
with open("palavras.txt", "r") as arquivo:
    conteudo_palavras = arquivo.read()

print("Conteúdo do arquivo 'palavras.txt':")
print(conteudo_palavras)