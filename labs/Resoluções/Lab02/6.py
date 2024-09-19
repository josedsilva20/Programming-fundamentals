"""
Escreva um programa em Python que lê três números e que diz qual o maior dos números lidos.

"""

QUANTIDADE = 3



def maior():
    antigo = float('-inf')
    quantidade = QUANTIDADE
    while (quantidade> 0):
        atual = eval(input("Digite o " + str(QUANTIDADE) + "º número -> "))
        if (atual > antigo):
            maior = atual
        antigo = atual
        quantidade -= 1
    
    print("O maior é -> " + str(maior))

maior()
