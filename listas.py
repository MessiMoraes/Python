"""
Listas em Python funcionam como matrizes/vetores (arrays) em outras linguagens, com diferença de
serem dinâmicos e também podemos colocar QUALQUER tipo de dados.

- Dinâmico: Não possui tamanho fixo
- As lista em Python são representadas por colchetes: []

"""
listaNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listaLetra = ['M', 'e', 's', 's', 'i']
listaVazia = []
listaRange = list(range(11))
listaNome = list("Messi")
listaVariada = [1, 2, 3, 'Messi', [100, 200, 300], 1.0, 1234567890]


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
# print(listaNome)
# listaNome = ' '.join(listaNome) #  Coloca espaço entre as strings
# # print(listaNome)

# nome = '$'.join(listaNome) #  Coloca o cifrão entre as strings
# print(nome)

# print(listaVariada)
#

# Iterando sobre a lista.
# soma = 0
# for elemento in listaNum:
#     print(elemento)
#     soma = soma + elemento
# print(soma)

# Utilizando while

# carrinho = []
# produto = ''
#
# while produto != 'sair':
#     print("Adicione um produto na lista ou digite 'sair' para sair: ")
#     produto = input()
#     if produto != 'sair':
#         carrinho.append(produto)
# print("Você saiu!")
#
# for produto in carrinho:
#     print(produto)
#

# Utilizando variaveis na lista
# numeros = [1, 2, 3]
# print(numeros)
#
# num1 = 1
# num2 = 2
# num3 = 3
#
# numeros = [num1, num2, num3]
# print(numeros)

# Acessamos os elementos de forma indexada
# cores = ['verde', 'amarelo', 'azul', 'branco']
# print(cores[0])
# print(cores[1])
# print(cores[2])
# print(cores[3])
#
# print('- - -')
# Acessar os elementos de forma indexada invresa

# print(cores[-1])
# print(cores[-2])
# print(cores[-3])
# print(cores[-4])

# for cor in cores:
#     print(cor)
#
# print(" - ")
#
# indice = 0
# while indice < len(cores):
#     print(cores[indice])
#     indice = indice + 1

# Gerar índice em um for
# for indice, cor in enumerate(cores):
#     print(f"{indice} => {cor}")

# Listas aceitam valores repetidos.
# lista = []
# lista.append(10)
# lista.append(200)
# lista.append(200)
# print(lista)

# Outros métodos úteis.
# Encontrar o índice de uma elemento na lista

numeros = [1, 2, 3, 1, 4, 5, 6, 7, 8, 9, 0, 4]

# Qual índice está o valor 6
# Caso não tenha o elemento na lista, será apresentado erro.
# print(numeros.index(6))
# print(numeros.index(5))

# Fazer busca dentro de um range a partir de um índice para começar o busca.
# print(numeros.index(4, 1))  # buscando a partir do índice 1
# print(numeros.index(4, 5))  # buscando a partir do índice 2

# Podemos fazer busca em um range, início/fim
# print(numeros.index(3, 1, 4))

# Revisão de slicing

# lista(inicio:fim:passo)
# range(inicio:fim:passo)

# trabalhando com slice de lista com o parâmetro 'Ínicio.
# print(listaNum[0::])  # Iniciando no indice 1 e pegando os elementos restantes.

# trabalhando com slice da lista com o parâmetro 'Fim'.
# print(listaNum[:2])  # Começa em 0 e pega até o índice 2 - 1.
# print(listaNum[:4])  # Começa em 0 e pega até o índice 3 - 1.
# print(listaNum[1:3])  # Começa em 1 e pega até o índice 3 - 1.

# trabalhando com slice de lista com parâmetro
# print(listaNum[1::2])  # Começa em 1, vai até o final de 2 em 2.
# print(listaNum[::2])
# print(listaNum[1::-1])

# Invertendo valores em uma lista.
# nome = ['Messi', 'Moraes']
# nome[0], nome[1] = nome[1], nome[0]
# print

# Soma, Valor Máximo, Valor Mínimo, Tamanho.
# Somente os valores inteiros ou reais.

# print(sum(listaNum))  # Soma
# print(max(listaNum))  # Valor Máximo
# print(min(listaNum))  # Valor Mínimo
# print(len(listaNum))  # Tamanho da lista

# Transformar lista em Tuplas.
# print(listaNum)
# print(type(listaNum))
#
# tupla = tuple(listaNum)
# print(tupla)
# print(type(tupla))

# Desempacotamento de listas
# lista = [1, 2, 3]
# num1, num2, num3 = lista
# print(num1)
# print(num2)
# print

# Copaindo uma lista para outra (Shallow Copy e Deep Copy)
# Forma 1 - Deep Copy
# lista = [1, 2, 3]
# print(lista)
# novaCopia = lista.copy()
# print(novaCopia)
# novaCopia.append(4)
# print(lista)
# print(novaCopia)

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

copia = lista
print(copia)

copia.append(4)
print(lista)
print(copia)













