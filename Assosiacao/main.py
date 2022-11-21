from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor("Joãozinho")   # Passando o nome direto
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()
# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = maquina  # ferramenta vai receber o objeto interio dos metodos
escritor.ferramenta.escrever()  # ação gerada pelos metodos na classe

del escritor

print(caneta.marca)
maquina.escrever()