"""
Recebendo dados do usuário
"""
# Entrada de dados
# print("Qual é o seu nome? ")
nome = input("Qual é o seu nome? ")

# print("Qual é a sua idade")
idade = int(input("Qual é a sua idade? "))
# Processamento

#Saída
# print("Seja vem vinda(a) %s " % nome) # saída na versão 2.x
# print('O %s tem %s anos. ' % (nome, idade)) # saída na versão 2.x

# print("Seja bem vindo(a) {0}.".format(nome)) # saída na versão 3.x
# print("O {0} tem {1} anos.".format(nome, idade)) # saída na versão 3.x

# print(f"Seja bem vindo(a) {nome}") # saída na versão 3.7
# print(f"O {nome} tem {idade} anos") # saída na versão 3.7

# int int(idade) cast é conversão de um tipo de dado para outro
print(f"{nome} nasceu em {2021 - int(idade)}.")
