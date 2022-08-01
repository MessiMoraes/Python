"""
Loop for
Loop é uma estrutura de repetição.
For é uma dessas estruturas.

Utilizamos loops para iterar sobre sequências ou sobre valores

Exemplos:
    - Strings
    - Listas
    - Range
"""

nome = 'Messi'
lista = [10, 20, 30, 40]
numeros = range(1, 10)  # Será transformado em lista

# for letra in nome:
#     print(letra)


# for item in lista:
#     print(item)


# for numero in numeros:
#     print(numero)


#  Quando não precisamos de um valor, podemos descartá-los utilizando um undeline (_)
# for i, v in enumerate(nome):
#     print(f"{i} -> {v}")

#  Imprime índice e o valor
# for v in enumerate(nome):
#     print(v)


# qtd = int(input("Quantas vezes esse loop deve rodas: "))
# soma = 0
#
# for n in range(1, qtd + 1):
#     num = int(input(f"Informe o {n} / {qtd} valor: "))
#     soma += num
# print(f"A soma é {soma}")

# nome = 'Messi Moraes'
# for letra in nome:
#     print(letra, end='')

emoji = 'U0001f60D'

for _ in range(3):
    for num in range(1, 11):
        print('\U0001f60D' * num)

