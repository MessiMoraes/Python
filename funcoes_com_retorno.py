"""
Funções com retorno
Funções Python que retornam valores, devem retornar esses valores com a palavra reservada return.

"""


# numeros = [1, 2, 3]
# r = numeros.pop()
# print(r)

# def quadadro_de_sete():
#    return 7 * 7
#
#
# r = quadadro_de_sete()
# print(r)
# print(quadadro_de_sete())

# def nova_funcao():
#     variavel = False
#     if variavel:
#         return 4
#     elif variavel is None:
#         return 3.2
#     return 'b'
#
# print(nova_funcao())

# def outra_funcao():
#    return 2, 3, 4, 5

# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

# print(outra_funcao())
# print(type(outra_funcao()))

# Função para jogar moeda
# from random import random
# def joga_moeda():
#    # Gera um número pseudo-randômico entre 0 e 1
#    if random() > 0.5:
#       return 'Cara'
#    return 'Coroa'
#
# print(joga_moeda())

def e_impar():
   numero = 62
   if numero % 2 != 0:
      return 'Impar'
   return 'Par'

print(e_impar())




