"""
Listas em Python funcionam como matrizes/vetores (arrays) em outras linguagens, com diferença de
serem dinâmicos e também podemos colocar QUALQUER tipo de dados.

- Dinâmico: Não possui tamanho fixo
- As lista em Python são representadas por colchetes: []

"""
listaNum = [50, 50, 50, 50, 90, 100, 10, 20, 30, 40]
listaLetra = ['M', 'e', 's', 's', 'i']
listaVazia = []
listaRange = list(range(11))
listaNome = list("Messi")

# Podemos checar se determinado valor está contido na lista
# num = 10
# if num in listaRange:
#     print(f"Número {num} encontrado.")
# else:
#     print(f"Número {num} não encontrado.")

# if 'm' in listaLetra:
#     print("Encontrei a letra M")
# else:
#     print("Não encontrei a letra M")
#

# Podemos ordenar uma lista
# print(listaNum)
# listaNum.sort()
# print(listaNum)

# Contar ocorrências em uma lista
# print(listaNum.count(50))
# print(listaNome.count('s'))

# Adicionar um elemento em listas utilizando a função append.O elemento será sempre adicionado no final da lista.
# listaNum.append(250)
# listaNum.append([1, 2, 3]) # Adiciona na lista como elemento único.
# print(listaNum)

# if [1, 2, 4] in listaNum:
#     print("Encontrei na lista")
# else:
#     print("Não encontrei na lista")

# listaNum.extend([1001, 1002, 1003]) # Coloca cada elemento da lista como valor adicional da lista.
# print(listaNum)
#
# listaNum.extend('Messi')
# print(listaNum)

# Adicionar um novo elemento informando a posição do índice. Deslocando o valor existente para a direita.
# print(listaNum)
# listaNum.insert(2, 'Novo Valor')
# print(listaNum)

# Ajutando duas listas.
# lista = listaNum + listaNome
# listaNum.extend(listaNome)
# print(listaNum)

# Forma 01
# listaNum.reverse()
# listaNome.reverse()
# print(listaNum)
# print(listaNome)

# Forma 02
# print(listaNum[::-1]) # Slice
# print(listaNome[::-1]) # Slice

# Copiar uma lista
# listaCopia = listaNum.copy()
# print(listaCopia)

# Conta quantos elementos existem na lista.
# print(len(listaNum)

# Remover último elemento da lista.
# print(listaNum)
# print(listaNum.pop())  # Retorna último elemento removido
# print(listaNum)

# Remove um elemto pelo índice
# print(listaNum)
# print(listaNum.pop(2))
# print(listaNum)

# Remover todos os elementos
# print(listaNum)
# listaNum.clear()
# print(listaNum)

# Repetir elementos em uma lista.
# lista = [1, 2, 3]
# print(lista)
# lista = lista * 2
# print(lista)

# Converter string para lista

# Exemplo 01
# nome = 'Messi de Moraes'
# print(nome)
# nome = nome.split()  # Split sempara os elementos da lista pelo espaço entre elas.
# print(nome)

# Exemplo 02
# nome = 'Messi,de,Moraes'
# print(nome)
# nome = nome.split(',')  # Separa os elementos pela ",".
# print

# Convertendo lista em string.
print(listaNome)
listaNome = ' '.join(listaNome)
print(listaNome)














