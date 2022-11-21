# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)

class Pessoa:

    def __init__(self,nome):
        self._nome = nome

    @property  # atibuto não utiliza ()
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

p1 = Pessoa('Otávio')

print(p1.nome)
