"""
Saindo de loops com break.
Utilziamos o break para sair de loops de maneira projetada.
"""

# Exemplo 01
# for numero in range(1, 11):
#     if numero == 4:
#         break
#     else:
#         print(numero)
# print("Saiu do loop")

# Exemplo 02
while True:
    comando = input("Digite sair para sair: ")
    if comando == 'sair':
        break
