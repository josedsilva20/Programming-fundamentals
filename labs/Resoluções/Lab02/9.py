"""
## 9.
Escreva um programa em Python que lê uma sequência de dígitos, sendo cada um dos
dígitos fornecido numa linha separada, e calcula o número inteiro composto por
esses dígitos, pela ordem fornecida. Para terminar a sequência de dígitos é
fornecido ao programa o inteiro $-1$. O seu programa deve permitir a interação:

    `Escreva um dígito`

    `(-1 para terminar)`

    `? 3`

    `Escreva um dígito`

    `(-1 para terminar)`

    `? 2`

    `Escreva um dígito`

    `(-1 para terminar)`

    `? 5`

    `Escreva um dígito`

    `(-1 para terminar)`

    `? 7`

    `Escreva um dígito`

`(-1 para terminar)`

`? -1`

`O número é: 3257`

"""


def numero():
    soma = 0
    valor = 0

    while (valor >= 0 and valor != -1):
            soma = soma * 10
            soma += valor
            valor = eval(input("Escreva um dígito\n(-1 para terminar)\n? "))
    
    return "O número é: " + str(soma)


numero()