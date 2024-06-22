# Solicita o comprimento do terreno ao usuário e converte para inteiro
comprimento = int(input("Digite o comprimento do terreno em metros: "))

# Solicita a largura do terreno ao usuário e converte para inteiro
largura = int(input("Digite a largura do terreno em metros: "))

# Solicita o preço do metro quadrado ao usuário e converte para ponto flutuante
preco_m2 = float(input("Digite o preço do metro quadrado: "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprime o resultado formatado com duas casas decimais e com milhar separador
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")