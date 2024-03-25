class Cliente:
    def __init__(self, nome, sobrenome, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email


meu_cliente = Cliente("")
print(meu_cliente.nome)
print(meu_cliente.sobrenome)
print(meu_cliente.email)
