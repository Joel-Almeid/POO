class Cliente:
    def __init__(self):
        self.nome = None
        self.CPF = None
        self.saldo = None

class Produto:
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.tipo = None
        self.preço = None
        self.Cliente = None

    cliente1 = Cliente()
    cliente1.nome = ''
    cliente1.CPF = ''
    cliente1.saldo = 0

    prod1 = Produto()
    prod1.marca = 'Fiat'
    prod1.Modelo = 'Strada'
    prod1.tipo = "automotor"
    prod1.preco = "10000"
    prod1.Cliente = 'Cliente1'

    x = prod1.Cliente.nome
    print(x)



## o que e objeto ? instancia dde uma classe
##o que é uma instancia? ela ta mais ligada a versao do que exemplo: pessoa e uma classe ser humano e uma classe e a fernanda e a imstamcia de uma classe
## cria um objeto e instanciar objeto
