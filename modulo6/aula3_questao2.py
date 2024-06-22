urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = []

for url in urls:
    inicio = len("www.")
    fim = url.index(".com")
    nome_dominio = url[inicio:fim]
    dominios.append(nome_dominio)

print("dominios:", dominios)