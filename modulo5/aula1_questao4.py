import datetime

agora = datetime.datetime.now() # retorna um objeto datetime que contém a data e a hora atuais.

data_atual = f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}"
hora_atual = f"Hora: {agora.hour:02d}:{agora.minute:02d}"

print(data_atual)
print(hora_atual)