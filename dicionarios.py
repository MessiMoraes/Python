"""
Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.
Dicionários são coleções tipo chave/valor
Dicionário são representados por {}

Obs:
    - Chave e valor são separados por dois pontos 'chave': 'valor'
    - Tanto chave como valor, podem ser de qualquer tipo de dados.
    - Podemos misturar tipos de dados.

"""

# print(type({}))

# Forma 01
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PT': 'Portugal'}
print(paises)
print(type(paises))

# Forma 02 (Menos Comum)
paises = dict(BR='Brasil', EUA='Estados Unidos', PT='Portugal')
print(paises)
print(type(paises))