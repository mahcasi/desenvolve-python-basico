genero = input("Digite seu gênero (M ou F): ")
idade  = int(input("Digite sua idade: "))
tempo  = int(input("Digite seu tempo de serviço (em anos): "))

print((genero == 'F' and idade > 60 or tempo > 30 or (idade >= 60 and tempo >= 25)) or (genero == 'M' and idade > 65 or tempo > 30 or (idade >= 60 and tempo >= 25)))