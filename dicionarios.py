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
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PT': 'Portugal', 'RU': 'Russia'}
# print(paises)
# print(type(paises))
#
# # Forma 02 (Menos Comum)
# paises = dict(BR='Brasil', EUA='Estados Unidos', PT='Portugal')
# print(paises)
# print(type(paises))

# Acessando elementos
# Forma 01 - Acessando via chave, da mesma forma que a lista/tupla.
# print(paises['BR'])
# print(paises['PT'])

# Forma 02 - Acessando via get - Recomendada
# print(paises.get('BR'))
# print(paises.get('x'))

# Tipo de dado None em python representa o tipo sem tipo, ou tipo vazio.
# Podemos utilizar None quando queremos criar uma variável e inicializá-la com tipo sem tipo, antes receber valor
# final.
# Tipo None e sempre considerado com False.

# none = None
# print(none)
# print(type(none))
#
# numeros = 1.44, 1.34, 5.64
# print(numeros)
# print(type(numeros))

# russia = paises.get('JP')
# if russia:
#     print('Encontrei o pais')
# else:
#     print('Não encontrei o pais')

# Caso o get não encontre o objeto com a chave informada, será retornado o valor None e não será gerado KeyError
# pais = paises.get('EUA', 'Não encontrado')
# print(f'Encontrei o país: {pais}')

# print('BR' in paises)
# print('RU' in paises)
# print('EUA' in paises)
#
# if 'RU' in paises:
#     russia = paises['RU']
#     print(russia)

#  Podemos usar qualquer tipo de dados (int, float, string, boolean), lista, tupla dicionário como chaves de
#  dicionário.

# Tuplas por exemplo, são bastante interessante de serem utilizadas como chave de dicionários. Pois são imutáveis

# localidades = {
#     (35.6895, 39.6917): 'Tókyo',
#     (40.7128, 74.0060): 'Nova York',
#     (35.6890, 39.6920): 'São Paulo',
# }
#
# print(localidades)
# print(type(localidades))

# Adicionar elementos em um dicionário.
receita = {'jan': 100, 'fev': 200, 'mar': 300}
# print(receita)
# print(type(receita))

# Forma 01 - Mais comum
# receita['abr'] = 350
# print(receita)

# forma 02
# novo_dado = {'mai': 500}
# receita.update(novo_dado)
# print(receita)

# Atualizando dados em um dicionário
# Forma 01
# receita['mai'] = 550
# print(receita)

# Forma 02
# receita.update({'mai': 600})
# print(receita)

# 1 - Forma de adicionar ou atualizar elementos em um dicionário é a mesma.
# 2 - Não podemos ter chaves repetidas.

# Remover dados de um dicionário
# Forma 01 - Mais comum
# print(receita)
# retorno = receita.pop('mar')
# print(retorno)
# print(receita)

# Precisamo sempre informar a chave e caso não encontre o elemento, um KeyError e retornado.
# Ao remover um objeto o valor desse objeto é sempre retornado.

# Forma 02
# del receita['fev']
# print(receita)

# Se a chave não existir será gerado um KeyError
# Obs: Neste caso o valor removido não e retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras no qual adicionamos um produto.

"""
Carrinho de compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
"""

# 1 - Poderiámos utilizar uma lista para isso? Sim!

# carrinho = []
#
# produto1 = ['Playstation 04', 1, 2300.00]
# produto2 = ['God of War 04', 1, 150.00]
#
# carrinho.append(produto1)
# carrinho.append(produto2)
#
# print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? Sim!

# produto1 = ('Playstation 04', 1, 2300.00)
# produto2 = ('God of Wor', 1, 150.00)
#
# carrinho = (produto1, produto2)
# print(carrinho)

# 3 - Poderiamos utilizar o Dicionário para isso? Sim.

# carrinho = []
# produto1 = {'nome': 'Playstation 04', 'quantidade': 1, 'preco': 230.00}
# produto2 = {'nome': 'God of War', 'quantidade': 1, 'preco': 150.00}
#
# carrinho.append(produto1)
# carrinho.append(produto2)
#
# print(carrinho)

# Desta forma, facilmente adicionamos e removemos produtos no carrinho em cada produto.
# Podemos ter a certeza sobra cada informação

# Métodos de dicionários
# d = dict(a=1, b=2, c=3)
# print(d)
# print(type(d))

# Limpar o dicionário
# d.clear()
# print(d)

# Copiando dicionário para outro.
# Forma 01 Deep Copy
# novo = d.copy()
# print(novo)
#
# novo['d'] = 4
# print(d)
# print(novo)

# Forma 01 Shallow Copy
# novo = d
# print(novo)
# novo['d'] = 4
#
# print(d)
# print(novo)

# Forma não usual de criar dicionários
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# Métodos fromkeys recebe dois parâmetros: um iterável e uma valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

