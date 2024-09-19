"""
Escreva um programa em Python que lê um número inteiro positivo e produz o número correspondente a inverter a ordem dos seus dígitos. Por exemplo,

`Escreva um inteiro positivo`

`? 7633256`

`O número invertido é 6523367`
"""

def inverte():
    numero = eval(input("Escreva um inteiro positivo: "))
    copia = 0

    while (numero > 0):
        copia = copia * 10 + numero % 10
        numero = numero // 10
        
    return "Resultado: " + str(copia)

print(inverte())