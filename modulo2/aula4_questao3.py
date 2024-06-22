produto1_nome = input("Digite o nome do produto 1: ")
produto1_preco = float(input("Digite o preço unitário do produto 1: "))
produto1_quantidade = int(input("Digite a quantidade do produto 1: "))

produto2_nome = input("Digite o nome do produto 2: ")
produto2_preco = float(input("Digite o preço unitário do produto 2: "))
produto2_quantidade = int(input("Digite a quantidade do produto 2: "))

produto3_nome = input("Digite o nome do produto 3: ")
produto3_preco = float(input("Digite o preço unitário do produto 3: "))
produto3_quantidade = int(input("Digite a quantidade do produto 3: "))

# Calcular o preço total de cada produto
total_produto1 = produto1_preco * produto1_quantidade
total_produto2 = produto2_preco * produto2_quantidade
total_produto3 = produto3_preco * produto3_quantidade

# Calcular o preço total da compra
total_compra = total_produto1 + total_produto2 + total_produto3

#Duas casas decimais, separador de milhar e ponto flutuante
print(f"Total: R${total_compra:,.2f}")