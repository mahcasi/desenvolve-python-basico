n = int(input("Digite a quantidade de respondentes: "))

soma = 0 
cont = 0 # variavel do controle de laço

while cont < n:
    idade = int(input(f"Digite a idade do respondente {cont + 1}: "))
    soma = soma + idade # soma += idade
    cont = cont + 1 # cont += 1

print(f"A média das idades é: {soma/n:.2f} anos.")

