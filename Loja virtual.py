class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def total(self):
        return sum([produto.preco for produto in self.produtos])

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = Carrinho()

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, id):
        self.produtos = [produto for produto in self.produtos if produto.id != id]

# Exemplo de uso
loja = Loja("Loja Virtual")
loja.adicionar_produto(Produto(1, "Camiseta", 50.0))
loja.adicionar_produto(Produto(2, "Calça", 100.0))

cliente = Cliente("João")
cliente.carrinho.adicionar_produto(loja.produtos[0])

print(f"Total do carrinho: {cliente.carrinho.total()}")
