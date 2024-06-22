top_musicas = []

with open('spotify-2023.csv', mode='r', encoding='latin-1') as arquivo:
    linhas = arquivo.readlines()
    cabecalho = linhas[0].strip().split(',')  # Obter cabeçalho e separar por vírgula
    
    for linha in linhas[1:]:
        # Dividir a linha em colunas, considerando a vírgula como separador
        colunas = linha.strip().split(',')
        
        # Extrair informações das colunas necessárias
        nome_musica = colunas[0].strip('"')  # Remover aspas da coluna nome_musica
        
        # Extrair nome_artista(s) e contar número de artistas
        info_artista = colunas[1].strip('"')
        if info_artista.startswith('"') and info_artista.endswith('"'):
            # Caso especial para nome_artista(s) com mais de um artista
            nome_artista = info_artista[1:-1].replace('",', ',')
            qtd_artistas = nome_artista.count(',') + 1
        else:
            # Caso comum para nome_artista(s) com um único artista
            nome_artista = info_artista
            qtd_artistas = 1
        
        # Extrair ano_lancamento
        info_lancamento = colunas[3].strip().strip('"')  # Remover aspas e espaços extras
        if info_lancamento.isdigit():  # Verificar se info_lancamento é um número
            ano_lancamento = int(info_lancamento)
        else:
            continue  # Ignorar esta linha se info_lancamento não for um número
        
        # Extrair streams corretamente (nona coluna, índice 8)
        info_streams = colunas[8].strip()
        if info_streams.isdigit():  # Verificar se info_streams é um número
            streams = int(info_streams.replace(',', ''))  # Converter streams para inteiro, removendo vírgulas
        else:
            continue  # Ignorar esta linha se info_streams não for um número
        
        # Verificar se a música está dentro do intervalo de 2012 a 2022
        if 2012 <= ano_lancamento <= 2022:
            # Ignorar linhas com mais de um artista e que estão com dados incorretamente formatados
            if qtd_artistas == 1 and colunas[0][0] != '"':
                # Verificar se já existe uma música desse ano na lista top_musicas
                encontrou = False
                for i in range(len(top_musicas)):
                    if top_musicas[i][2] == ano_lancamento:
                        encontrou = True
                        # Atualizar se esta música tem mais streams do que a já registrada
                        if streams > top_musicas[i][3]:
                            top_musicas[i] = [nome_musica, nome_artista, ano_lancamento, streams]
                
                # Se não encontrou, adiciona à lista top_musicas
                if not encontrou:
                    top_musicas.append([nome_musica, nome_artista, ano_lancamento, streams])

# Ordenar a lista top_musicas por ano_lancamento
top_musicas.sort(key=lambda x: x[2])

# Imprimir a lista final
print(top_musicas)