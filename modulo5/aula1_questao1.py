num1 = float(input("Digite o primeiro número decimal: "))
num2 = float(input("Digite o segundo número decimal: "))

diferenca_absoluta = abs(num1 - num2) # Calcula a diferença absoluta entre os dois números
diferenca_absoluta = round(diferenca_absoluta, 2) # Arredonda o resultado para duas casas decimais

print(f"A diferença absoluta entre os números é: {diferenca_absoluta}")