import random

def embaralhar_palavras(frase):
    # Dividir a frase em palavras
    palavras = frase.split()
    resultado = []
    
    for palavra in palavras:
        # Se a palavra tiver 3 ou mais caracteres, embaralha as letras intermediárias
        if len(palavra) > 2:
            # Converte a palavra em uma lista de caracteres (para poder embaralhar)
            letras = list(palavra)
            
            # Embaralha as letras intermediárias (começa do segundo e vai até o penúltimo)
            meio = letras[1:-1]
            random.shuffle(meio)
            
            # Reconstrói a palavra com as letras embaralhadas
            palavra_embaralhada = letras[0] + ''.join(meio) + letras[-1]
        else:
            # Se a palavra tem menos de 3 caracteres, mantém ela como está
            palavra_embaralhada = palavra
        
        # Adiciona a palavra (embaralhada ou não) ao resultado
        resultado.append(palavra_embaralhada)
    
    # Junta as palavras de volta em uma frase
    frase_embaralhada = ' '.join(resultado)
    
    return frase_embaralhada

# Exemplo de uso:
frase = input("Digite uma frase para embaralhar: ")
resultado = embaralhar_palavras(frase)
print(resultado)