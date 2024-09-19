"""
Escreva um programa em Python que lê um número inteiro positivo e produz o número correspondente a inverter a ordem dos seus dígitos. Por exemplo,

`Escreva um inteiro positivo`

`? 7633256`

`O número invertido é 6523367`
"""

def inverte():
    numero = eval(input("Escreva um inteiro positivo: "))
    res = 0
    expoente = 0
    tuplo = ()

    if numero <= 0:
        numero = eval(input("Precis ser inteiro positivo :( -> "))


    while numero >= 1:
        aux = numero % 10
        tuplo += (aux,)
        expoente += 1
        numero = numero // 10

    for i in range (len(tuplo)):
        expoente -= 1
        res += tuplo[i] * 10 ** expoente


    print("O numero invertido é: " + str(res))

inverte()