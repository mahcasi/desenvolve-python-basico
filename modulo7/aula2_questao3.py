caracteres_permitidos = "abcdefghijklmnopqrstuvwxyz0123456789"

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if frase.lower() == 'fim':
        break
    
    # Remove espaços em branco, pontuações e converte para minúsculas
    frase_limpa = ''
    for caractere in frase:
        if caractere.lower() in caracteres_permitidos:
            frase_limpa += caractere.lower()
    
    # Verifica se a frase limpa é igual à sua inversa
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')