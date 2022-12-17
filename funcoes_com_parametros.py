"""
Funções com parâmetro de entrada
 - Funcões que recebem dados para serem processados.
"""


# def quadadro(q):
#     return q ** 2
#
# print(quadadro(5))
#
#
# def soma(a, b):
#     return a + b
#
# print(soma(10, 5))

# def outra(num1, b, num2):
#     return (num1 + b) * num2
#
# print(outra(5, 2, 'Messi '))

# Nomeando Parâmentros
def nome_completo(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'
print(nome_completo('Messi', 'Moraes'))

# Diferença entre Parâmetros e Argumentos
# - Parâmetros são variáveis declaradas na definição da função
# - Argumentos são os dados passados durante a execução de  função

# A ordem dos parâmetros importa.


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5)
print(soma_impares(tupla))
