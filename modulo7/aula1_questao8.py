def calcular_digito_verificador(cpf, multiplicadores):
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    # Remove os caracteres de formatação
    cpf = cpf.replace('.', '').replace('-', '')

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    multiplicadores_primeiro_digito = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    primeiro_digito = calcular_digito_verificador(cpf[:9], multiplicadores_primeiro_digito)

    # Calcula o segundo dígito verificador
    multiplicadores_segundo_digito = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    segundo_digito = calcular_digito_verificador(cpf[:9] + str(primeiro_digito), multiplicadores_segundo_digito)

    # Verifica se os dígitos verificadores calculados são iguais aos fornecidos
    return cpf[9] == str(primeiro_digito) and cpf[10] == str(segundo_digito)

# Solicita o CPF do usuário
cpf_usuario = input("Digite seu CPF (XXX.XXX.XXX-XX): ")

# Verifica se o CPF é válido
if validar_cpf(cpf_usuario):
    print("Válido")
else:
    print("Inválido")