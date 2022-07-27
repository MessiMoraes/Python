"""
Escopo de

Dois casos de escopo:

1 - Variável Globais;
    - Variáveis globais são reconhecidas. Seu escopo compreende todo o programa.

2 - Variável Local;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas. Seus escopo esta limitado ao bloco de
    sua declaração.

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declaramos uma variável, nós não
colocamos o tipo de dados dela. Este tipo e inferido ao atribuírmos o valor da mesma.


"""

numero = 42
# print(type(numero))
# print(numero)
#
#
# texto = "Messi"
# print(type(texto))
# print(texto)

# novo = 0

if numero > 10:
    novo = numero + 10  # A variável novo esta declarada localmente dentro do bloco if. Portando, é loca.
    print(novo)

print(novo)


