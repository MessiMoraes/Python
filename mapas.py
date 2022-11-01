"""
Mapas -> Conhecidos em python como dicionários.
Dicionários em Python são representados por chaves.
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

# Interar sobre dicionários
# for chave in receita:
#     print(chave)
#
# for chave in receita:
#     print(receita[chave])
#
# for chave in receita:
#     print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves
# print(receita.keys())
# # print(receita.values()) # Acessando os valores
#
# for chave in receita.keys():
#     print(receita[chave])

# Acessando os valores
# for valor in receita.values():
#     print(valor)
#

# Desempacotamento de dicionários
# for chave, valor in receita.items():
#     print(f'chave= {chave} e valor= {valor}')

# *Soma, *Valor Máximo, *Valor Mínimo e Tamanho.
# *Se os valores forem todos inteiros ou reais.
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
