import os

# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Nome do arquivo
nome_arquivo = "frase.txt"

# Abre o arquivo em modo de escrita e salva a frase
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(frase)

# Obtém o caminho completo do arquivo salvo
caminho_completo = os.path.abspath(nome_arquivo)

# Imprime o caminho completo do arquivo salvo
print(f"O arquivo foi salvo em: {caminho_completo}")