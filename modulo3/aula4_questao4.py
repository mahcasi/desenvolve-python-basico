distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))

if distancia <= 100:
    custo_frete = peso * 1
elif distancia >= 101 and distancia <= 300:
    custo_frete = peso * 1.5
else:
    custo_frete = peso * 2

if peso > 10:
    custo_frete += 10

print (f"Frete = R${custo_frete}")
 
