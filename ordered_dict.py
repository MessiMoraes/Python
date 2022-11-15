"""
Módulo Collections: Ordered Dict
"""

# Em dicionário, a ordem de insersão dos elementos não são garantida.
# dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#
# for chave, valor in dicionario.items():
#     print(f'chave = {chave} : valor = {valor}')

# OrderedDict -> É um dicionário que nos garante a ordem de inserção dos elementos.

# Import
from collections import OrderedDict
# dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
#
# for chave, valor in dicionario.items():
#     print(f'chave -> {chave} valor -> {valor}')

# Difereça entre Dict e OrderedDict

# Dict
# dictOne = {'a': 1, 'b': 2}
# dictTwo = {'b': 2, 'a': 1}
# print(dictOne == dictTwo)  # True -> Já que a ordem dos elementos não importa para os dicionário

# Ordered Dict
# dictOne = OrderedDict({'a': 1, 'b': 2})
# dictTwo = OrderedDict({'b': 2, 'a': 1})
# print(dictOne == dictTwo)  # False -> Já que a ordem dos elementos importa para o OrderedDict



