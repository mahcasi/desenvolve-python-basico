import random

def escolhe_palavra():
    # Abre o arquivo "gabarito_forca.txt" e escolhe uma palavra aleatória
    with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
    
    palavra = random.choice(palavras).strip().lower()  # Escolhe uma palavra aleatória e remove espaços em branco
    
    return palavra

def carrega_estagios_enforcado():
    # Abre o arquivo "gabarito_enforcado.txt" e carrega os estágios do enforcado
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
        estagios_enforcado = arquivo.read().strip().split("\n\n")
    
    return estagios_enforcado

def imprime_enforcado(erros):
    # Função para imprimir o enforcado de acordo com o número de erros
    print(estagios_enforcado[erros])

def jogo_da_forca():
    palavra = escolhe_palavra()
    tamanho_palavra = len(palavra)
    letras_descobertas = ['_'] * tamanho_palavra
    letras_tentadas = []
    erros = 0
    
    print("Bem-vindo ao jogo da Forca!")
    print(f"A palavra que você deve adivinhar tem {tamanho_palavra} letras.")
    print(" ".join(letras_descobertas))  # Mostra a palavra como underscores
    
    while '_' in letras_descobertas and erros < 6:
        letra = input("\nDigite uma letra: ").lower()
        
        if letra in letras_tentadas:
            print(f"Você já tentou a letra '{letra}'. Tente outra letra.")
            continue
        
        letras_tentadas.append(letra)
        
        if letra in palavra:
            for i in range(tamanho_palavra):
                if palavra[i] == letra:
                    letras_descobertas[i] = letra
            print(" ".join(letras_descobertas))
        else:
            erros += 1
            imprime_enforcado(erros)
    
    if '_' not in letras_descobertas:
        print("\nParabéns! Você acertou a palavra.")
    else:
        print(f"\nGame over! A palavra era '{palavra}'.")

# Carrega os estágios do enforcado
estagios_enforcado = carrega_estagios_enforcado()

# Executa o jogo da forca
jogo_da_forca()