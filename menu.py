from produto import Produto

produtos = []

def adicionar_produto():
    nome = input("Nome do produto: ")
    try:
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))
        novo_produto = Produto(nome, preco, quantidade)
        produtos.append(novo_produto)
        print("Produto adicionado!")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

def exibir_produtos():
    if produtos:
        for produto in produtos:
            produto.exibir_informacoes()
            print("-" * 20)
    else:
        print("Nenhum produto cadastrado.")

def atualizar_preco():
    nome = input("Nome do produto para atualizar o preço: ")
    produto = next((p for p in produtos if p.nome == nome), None)
    if produto:
        try:
            novo_preco = float(input("Novo preço: "))
            produto.atualizar_preco(novo_preco)
        except ValueError:
            print("Erro: O preço deve ser numérico.")
    else:
        print("Produto não encontrado.")

def atualizar_quantidade():
    nome = input("Nome do produto para atualizar a quantidade: ")
    produto = next((p for p in produtos if p.nome == nome), None)
    if produto:
        try:
            nova_quantidade = int(input("Nova quantidade: "))
            produto.atualizar_quantidade(nova_quantidade)
        except ValueError:
            print("Erro: A quantidade deve ser numérica.")
    else:
        print("Produto não encontrado.")

def menu_interativo():
    while True:
        print("\n1. Adicionar Produto")
        print("2. Exibir Produtos")
        print("3. Atualizar Preço")
        print("4. Atualizar Quantidade")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_produtos()
        elif opcao == "3":
            atualizar_preco()
        elif opcao == "4":
            atualizar_quantidade()
        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu_interativo()
