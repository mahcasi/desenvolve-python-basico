nome_arquivo = "estomago.txt"

# Abrir o arquivo para leitura com codificação latin-1
with open(nome_arquivo, "r", encoding="latin-1") as arquivo:
    # Ler todas as linhas do arquivo
    linhas = arquivo.readlines()

    # Imprimir o texto das primeiras 25 linhas
    print("Texto das primeiras 25 linhas:")
    for i in range(min(25, len(linhas))):
        print(linhas[i].strip())  # strip() para remover espaços em branco adicionais

    # Número total de linhas do arquivo
    num_linhas = len(linhas)
    print(f"\nNúmero de linhas do arquivo: {num_linhas}")

    # Encontrar a linha com maior número de caracteres
    maior_linha = max(linhas, key=len).strip()
    num_caracteres_maior_linha = len(maior_linha)
    print(f"\nLinha com maior número de caracteres:")
    print(f"{maior_linha} (Número de caracteres: {num_caracteres_maior_linha})")

    # Contagem de menções aos nomes dos personagens "Nonato" e "Íria"
    nome_personagens = ["Nonato", "Íria"]
    contagem_nonato = 0
    contagem_iria = 0

    for linha in linhas:
        linha_minuscula = linha.lower()  # Converter para minúsculas para facilitar a busca
        for nome in nome_personagens:
            contagem = linha_minuscula.count(nome.lower())
            if nome == "Nonato":
                contagem_nonato += contagem
            elif nome == "Íria":
                contagem_iria += contagem

    print(f"\nNúmero de menções aos nomes dos personagens:")
    print(f"Nonato: {contagem_nonato}")
    print(f"Íria: {contagem_iria}")