"""
Escreva um programa em Python que lê dois inteiros positivos
m e n e devolve o resultado da divisão inteira de m por n. 
Não pode, para este exercício, utilizar as operação aritméticas *, /, // e %.
"""


def divide(m, n):
    count       = 1
    count_aux   = 0
    if (m < n):
        return 0
    
    if (m == n):
        return 1
    
    for i in range(n, m):
        count_aux += 1     
        if (count_aux == n):
            count += 1
            count_aux = 0
    
    return count


print(divide(eval(input("Digite o 1º número: ")),eval(input("Digite o 2º número: "))))
