n = int(input("Digite a quantidade de experimentos registrados: "))

total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

cont = 0

while cont < n:
    quantia = int(input(f"Digite a quantidade de cobaia no experimento {cont + 1}: "))
    tipo = input("Digite o tipo das cobaias (S, R ou C): ")

    total_cobaias += quantia
    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

    cont += 1

percentual_sapos = (total_sapos / total_cobaias) * 100 
percentual_ratos = (total_ratos / total_cobaias) * 100 
percentual_coelhos = (total_coelhos / total_cobaias) * 100 

print(f"Total de cobaias: {total_cobaias}")
print(f"Total de sapos: {total_sapos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")