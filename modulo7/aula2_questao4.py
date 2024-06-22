def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Variáveis de controle para verificar a presença de cada tipo de caractere
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    # String com caracteres especiais permitidos
    caracteres_especiais = "@#$"
    
    # Verifica cada caractere da senha
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in caracteres_especiais:
            tem_especial = True
        
        # Se todos os critérios forem atendidos, podemos parar a verificação
        if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
            break
    
    # Retorna True se todos os critérios forem atendidos, caso contrário retorna False
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

print("A senha deve ter pelo menos 8 caracteres, conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial (@, #, $).")
senha = input("Digite sua senha: ")

# Verifica se a senha é válida usando a função validador_senha()
if validador_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")