"""
Módulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance.

"""
# Import
from collections import deque

# Criando Deque

deq = deque('Messi')
print(deq)

# Adicionando elementos no Deque
deq.append('Moraes')  # Adiciona no final
print(deq)

deq.appendleft('Moraes')  # Adiciona no começo
print(deq)

# Remover elementos
deq.pop()  # Remove e retirna o último elemento
print(deq)

deq.popleft()  # Remove e retirna o primeiro elemento
print(deq)
