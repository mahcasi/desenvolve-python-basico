idade = int(input("Digite sua idade: "))
jogou_3_jogos = input("Já jogou pelos menos 3 jogos de tabuleiro? True/False): ")
jogos_vencidos = int(input("Quantos jogos já venceu? "))

print (idade > 15 and idade < 19 and jogou_3_jogos and jogos_vencidos >= 1)
