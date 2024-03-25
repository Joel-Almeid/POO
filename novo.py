class Cliente:
    def __init__(self):
        self.nome = ""
        self.CPF = ""
        self.saldo = 0
class Produto:
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.tipo = None
        self.preco = None
        self.Cliente = None

clientel = Cliente()
clientel.nome = ''
clientel.CPF = ''
clientel.saldo = 0

prod1 = Produto()
prod1.marca = 'Fiat'
prod1.modelo = 'Strada'
prod1.tipo = "automotor"
prod1.preco = "10000"
prod1.Cliente = clientel

x = prod1.Cliente.nome

print(prod1.marca)
