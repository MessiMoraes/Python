"""
Modulo Collections - Default Dict

"""
# Recapitulando Dicionários
# dicionario = {'curso': 'Programação em Python: Essencial'}
# print(dicionario)
# print(dicionario['curso'])

# Default Dict ->  Ao criar dicionário utilizando o default dict, nos informamos um valor default
# e podemos utlizar lambada para isso. Este valor será utilzado sempre que não ouver um valor definido.
# Se tentarmos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído

# Lambada são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores.

#Import
from collections import defaultdict
dicionario  = defaultdict(lambda: "Chave não localizada")
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro'])
print(dicionario)

