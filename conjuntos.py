"""
Conjuntos - Em qualquer linguagem de programação, estamos fazendo referência a teoria dos conjuntos da matemática.
- No Python os conjuntos são chamados de Sets.
- Na mesma forma que na matemática, conjuntos não possuem:
    - (Sets) Valores duplicados.
    - (Sets) Valores ordenados.
    - Não são indexados
    - Não são acessados via índice

- Usamos quando precisamos armazenas elementos, sem se importar com a ordenação, chaves, valores e itens duplicados.
- (Sets) são referenciados em Python com chaves {}.

Diferença entre Conjunto (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor.
    - Um conjunto tem apenas valor.

"""

# Definindo um conjunto
# Forma 01
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
# print(s)
# print(type(s))

# Criando o conjunto, caso seja adicionado um valor já existente o mesmo será ignorado, sem gerar erro e não fara parte
# do conjunto.

# Forma 02 -  Mais comum
# s = {1, 2, 3, 5, 5}
# print(s)
# print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto.
# if 3 in s:
#     print("tem o 3")
# else:
#     print("não tem o 3")

# Importante lembrar que, além de não termos valores duplicados. Não temos ordem.
# Lista aceitam valores duplicados.
# lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
# print(f'{lista} -> {len(lista)}')

# Tuplas aceitam valores duplicados.
# tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
# print(f'{tupla} -> {len(tupla)}')

# Dicionários não aceitam chaves duplicadas.
# dicionario = {}.fromkeys(lista, 'dict')
# print(f'{dicionario} -> {len(dicionario)}')

# Conjuntos não aceitam valores duplicados.
# conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
# print(f'{conjunto} -> {len(conjunto)}')

# Assim como todo outro conjunto Python podemos colocar, tipos de dados misturados em Set.
# s = {1, 'b', True, 34.22, 44}
# print(s)

# Podemos interar em um set normalmente.
# for valor in s:
#     print(valor)

# Usos interessantes com Sets

# Imagine que fizemos um formularios de cadastro de visitantes em uma feira ou museu
# Informam manualmente a cidade onde vieram
# Nós adicionamos cada cidade em uma lista em Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agoras precisamos saber quantas cidades distintas, ou seja, únicas, temos.
print(len(set(cidades)))


