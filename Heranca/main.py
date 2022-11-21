from classes import *

# c1_nome = input('Digite o nome do Cliente: ')
# c1_idade = int(input('Digite a idade do cliente: '))
# Cliente = c1_nome, c1_idade
# print(f'Cliente cadastrado: {Cliente} ')

c1 = Cliente('Luiz', 45)
c1.falar()
c1.comprar()

# a1 = Aluno('Maria', 54)
# a1.falar()
# a1.estudar()
#
# p1 = Pessoa('João', 43)
# p1.falar()
print()
c2 = ClienteVIP('Rose', 25, 'Miranda')
c2.falar()