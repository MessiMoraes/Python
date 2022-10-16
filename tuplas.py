"""
Tuplas(Tuple)
Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças.
1 - As tuplas são representadas por parênteses()
2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em um tupla
gera uma nova tupla.
"""

# As tuplas são representadas por ()
# tupla = (1, 2, 3)  # tuplas com ()
# print(tupla)
# print(type(tupla))

# tupla = 1, 2, 3  # tuplas sem ()
# print(tupla)
# print(type(tupla))

# Tuplas com 1 elemento
# tupla = (3)  # não é uma tupla
# print(tupla)
# print(type(tupla))

# Podemos concluir que tupla são definidas por "," e não pelo uso dos parênteses.
# tupla = (4, ) #Isso também é uma tupla
# print(tupla)
# print(type(tupla))

# Podemos gerar uma tupla dinamicamente com range(início, fim e passo)
# tupla = tuple(range(10))
# print(tupla)
# print(type(tupla))

# Desempacotamento de tupla
# Gera erro (ValueError) se colocarmos num numero diferente de elementos para desempacotamento.

# tupla = ('Messi', 'Moraes')
# nome, sobrenome = tupla
# print(nome)
# print(sobrenome)

# Métodos para adição e remoção de elemento nas tuplas não existe. Tuplas são imutáveis
# Soma, Valor Máximo, Valor Mínimo e tamanhos.
# Se os valores forem inteiros ou reais.

# tupla = (1.5, 2, 3, 4)
# print(sum(tupla))
# print(max(tupla))
# print(min(tupla))
# print(len(tupla))

# Concatenação de tuplas
# tuplaOne = (1, 2, 3)
# print(tuplaOne)
#
# tuplaTwo = (4, 5, 6)
# print(tuplaTwo)
#
# print(tuplaOne + tuplaTwo) # Tuplas são imutáveis.
# tuplaOne = tuplaOne + tuplaTwo
# print(tuplaOne)  # Mas podemos sobrescrever seus valores.

# Verificar se o elemento está na lista.
# tupla = (1, 2, 3)
# print(3 in tupla)

# Iterando sobra a tupla
# tupla = (1, 2, 3)
# for n in tupla:
#     print(n)
#
# for indice, valor in enumerate(tupla):
#     print(indice, valor)

# Contando elementos dentro da Tupla.
# tupla = ('a', 'a', 'b', 'b', 'b', 'c')
# print(tupla.count('a'))
# print(tupla.count('b'))
# print(tupla.count('c'))

# Dicas na utilização de tuplas.
# Devemos utilizar tuplas, sempre que não precisamos modificar os dados contidos em uma coleção.

# meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
#          'Novembro', 'Dezembro')

# print(meses)

# Acessar os elementos de uma tupla é semelhante a de uma lista.
# print(meses[10])

# iterar com While
# i = 0
# while i < len(meses):
#     print(meses[i])
#     i = i + 1

# Verificando pelo indice
# print(meses.index('Agosto', 7)) # Se o elemento não existir na será gerado um ValueError

# Slicing
# tupla[início: fim: passo]
# print(meses[0:12:2])

# Por que utilizar tuplas?
## Tuplas são mais rapidas do que listas.
## Tuplas deixam seu código mais seguro.
## Trabalhar com elementos imutáveis traz seguranca para código.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla
print(nova)
print(tupla)


