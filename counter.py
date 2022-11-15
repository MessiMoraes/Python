"""
Módulo Collection - Counter (Contador)
Collections -> High-Performance Container Date types

Counter -> Recebe um iteravel como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com dicinário, contendo como chave o elemento da lista passada como parâmentro e como valor
a quantidade de ocorrências desse elemento.
"""
#
# Realizando o import
from collections import Counter
# lista = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5]
# res = Counter(lista)
# print(type(res))
# print(res)

# Para cada elemento da lista o Counter criou uma chave e colocou como o valor a quantidade de ocorrências
# Counter({1: 3, 2: 2, 3: 2, 5: 2, 4: 1})

# print(Counter('Messi Moraes'))

text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry."""
word = text.split()
print(word)

res = Counter(text)
print(Counter(text))

# Encontrando as 5 palavras com mais ocorrência de texto
print(res.most_common(5))
