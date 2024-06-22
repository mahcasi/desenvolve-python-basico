data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = data_nascimento.split('/')

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Converte o mês de string para inteiro e acessa o nome do mês correto na lista
nome_mes = meses[int(mes) - 1]

print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")