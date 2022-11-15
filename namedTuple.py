"""
Módulo Collections - Named Tuple

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

# Import
from collections import namedtuple

# Precisamos definir o nome e parãmetros
# Forma 01 - Declaração
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 02 = Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 03 = Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
# print(ray)
# print(ray[0])  # Idade
# print(ray[1])  # Raça
# print(ray[2])  # Nome

# Forma 02
# print(ray.idade)  # Idade
# print(ray.raca)  # Raça
# print(ray.nome)  # Nome

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))


