import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    
    nomes_cript = [] 
    
    for nome in nomes:
        nome_criptografado = ""
        for caractere in nome:
            novo_caractere = chr(ord(caractere) + chave_aleatoria)
            if ord(novo_caractere) > 126:
                novo_caractere = chr(ord(novo_caractere) - 94)  # Voltar ao início do intervalo visível
            elif ord(novo_caractere) < 33:
                novo_caractere = chr(ord(novo_caractere) + 94)  # Ir para o final do intervalo visível
            
            nome_criptografado += novo_caractere
        
        nomes_cript.append(nome_criptografado)
    
    return nomes_cript, chave_aleatoria

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print("Chave de criptografia:", chave_aleatoria)
print("Nomes criptografados:", nomes_cript)