from pessoa import Pessoa

p1 = Pessoa('luiz', 29)  # instancia da classe ( self) se refere a estância]
p2 = Pessoa('João', 32)

print(Pessoa.gera_id())
print(p1.gera_id())
# # print(p1)
# # print(p1.nome, p1.idade)
# p1.get_ano_nascimento()
#
# # print(p1.get_ano_nascimento())
# # print(p2.get_ano_nascimento())
# #
# # # p1.comer('maça')
# # # # p1.parar_comer()
# # # # p1.parar_comer()
# # # # p1.comer('maça')
# # #
# # #
# # # # p2 = Pessoa('João', 32)
# # #
# # # # p1.nome = 'Luiz'
# # # # p2.nome = 'João'
# # # #
# # # # print(p2.nome)
# # # p1.falar('POO')
# # # p1.parar_comer()
# # # p1.falar('POO')
# # # p1.comer('alimento')
# # # p1.parar_falar()
# # # p1.comer('rapadura')
