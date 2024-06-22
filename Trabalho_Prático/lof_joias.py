import csv

# Estrutura de dados para armazenar os usuários
usuarios = {}
# Estrutura de dados para armazenar as peças
pecas = []

# Função para carregar usuários do arquivo CSV
def carregar_usuarios():
    with open('usuarios.csv', newline='') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            usuarios[linha['username']] = linha

# Função para carregar peças do arquivo CSV
def carregar_pecas():
    with open('pecas.csv', newline='') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            pecas.append(linha)

# Função para salvar usuários no arquivo CSV
def salvar_usuarios():
    with open('usuarios.csv', 'w', newline='') as arquivo_csv:
        cabecalho = ['username', 'nome', 'senha', 'permissao']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
        escritor.writeheader()
        for usuario in usuarios.values():
            escritor.writerow(usuario)

# Função para salvar peças no arquivo CSV
def salvar_pecas():
    with open('pecas.csv', 'w', newline='') as arquivo_csv:
        cabecalho = ['codigo', 'nome', 'preco', 'quantidade']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
        escritor.writeheader()
        for peca in pecas:
            escritor.writerow(peca)

# Função para adicionar um novo usuário
def adicionar_usuario(username, nome, senha, permissao):
    if username in usuarios:
        print("Usuário já existe!")
    else:
        usuarios[username] = {'username': username, 'nome': nome, 'senha': senha, 'permissao': permissao}
        salvar_usuarios()
        print("Usuário adicionado com sucesso!")

# Função para listar todos os usuários
def listar_usuarios():
    for usuario in usuarios.values():
        print(f"Username: {usuario['username']}, Nome: {usuario['nome']}, Permissão: {usuario['permissao']}")

# Função para remover um usuário
def remover_usuario(username):
    if username in usuarios:
        del usuarios[username]
        salvar_usuarios()
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado!")

# Função para adicionar uma nova peça
def adicionar_peca(codigo, nome, preco, quantidade):
    for peca in pecas:
        if peca['codigo'] == codigo:
            print("Peça já existe!")
            return
    pecas.append({'codigo': codigo, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
    salvar_pecas()
    print("Peça adicionada com sucesso!")

# Função para listar todas as peças
def listar_pecas():
    for peca in pecas:
        print(f"Código: {peca['codigo']}, Nome: {peca['nome']}, Preço: {peca['preco']}, Quantidade: {peca['quantidade']}")

# Função para buscar uma peça pelo nome ou código
def buscar_peca(termo):
    for peca in pecas:
        if peca['codigo'] == termo or peca['nome'].lower() == termo.lower():
            print(f"Código: {peca['codigo']}, Nome: {peca['nome']}, Preço: {peca['preco']}, Quantidade: {peca['quantidade']}")
            return
    print("Peça não encontrada!")

# Função para listar peças ordenadas por nome
def listar_pecas_ordenadas_por_nome():
    pecas_ordenadas = sorted(pecas, key=lambda x: x['nome'])
    for peca in pecas_ordenadas:
        print(f"Código: {peca['codigo']}, Nome: {peca['nome']}, Preço: {peca['preco']}, Quantidade: {peca['quantidade']}")

# Função para listar peças ordenadas por preço
def listar_pecas_ordenadas_por_preco():
    pecas_ordenadas = sorted(pecas, key=lambda x: float(x['preco']))
    for peca in pecas_ordenadas:
        print(f"Código: {peca['codigo']}, Nome: {peca['nome']}, Preço: {peca['preco']}, Quantidade: {peca['quantidade']}")

# Função para fazer login
def login(username, senha):
    if username in usuarios and usuarios[username]['senha'] == senha:
        return usuarios[username]['permissao']
    else:
        print("Credenciais inválidas!")
        return None

# Função principal
def main():
    carregar_usuarios()
    carregar_pecas()
    
    print("\n=== Sistema de Gerenciamento Lorena Joias ===")
    username = input("Username: ")
    senha = input("Senha: ")
    permissao = login(username, senha)
    
    if permissao:
        while True:
            print("\n=== Menu ===")
            if permissao == "gerente":
                print("1. Adicionar Usuário")
                print("2. Listar Usuários")
                print("3. Remover Usuário")
            print("4. Adicionar Peça")
            print("5. Listar Peças")
            print("6. Buscar Peça")
            print("7. Listar Peças Ordenadas por Nome")
            print("8. Listar Peças Ordenadas por Preço")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1" and permissao == "gerente":
                username = input("Username: ")
                nome = input("Nome: ")
                senha = input("Senha: ")
                permissao_user = input("Permissão: ")
                adicionar_usuario(username, nome, senha, permissao_user)
            elif opcao == "2" and permissao == "gerente":
                listar_usuarios()
            elif opcao == "3" and permissao == "gerente":
                username = input("Username: ")
                remover_usuario(username)
            elif opcao == "4":
                codigo = input("Código: ")
                nome = input("Nome: ")
                preco = input("Preço: ")
                quantidade = input("Quantidade: ")
                adicionar_peca(codigo, nome, preco, quantidade)
            elif opcao == "5":
                listar_pecas()
            elif opcao == "6":
                termo = input("Código ou Nome da Peça: ")
                buscar_peca(termo)
            elif opcao == "7":
                listar_pecas_ordenadas_por_nome()
            elif opcao == "8":
                listar_pecas_ordenadas_por_preco()
            elif opcao == "0":
                break
            else:
                print("Opção inválida ou permissão insuficiente!")
    else:
        print("Login falhou!")

if __name__ == "__main__":
    main()
