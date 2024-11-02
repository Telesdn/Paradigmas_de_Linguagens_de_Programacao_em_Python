class Produto:
    def __init__(self, nome, preco, quantidade):
        # Construtor da classe Produto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self):
        # Exibe as informações do produto
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

    def atualizar_preco(self, novo_preco):
        # Atualiza o preço do produto
        if novo_preco >= 0:
            self.preco = novo_preco
            print("Preço atualizado com sucesso!")
        else:
            print("Erro: Preço deve ser positivo.")

    def atualizar_quantidade(self, nova_quantidade):
        # Atualiza a quantidade do produto
        if nova_quantidade >= 0:
            self.quantidade = nova_quantidade
            print("Quantidade atualizada com sucesso!")
        else:
            print("Erro: Quantidade deve ser não negativa.")
