"""
Escreva um programa em Python que pede ao utilizador que lhe forneça uma sucessão
de inteiros correspondentes a valores em segundos e que calcula o número de dias
correspondentes a cada um desses inteiros. 
O programa termina quando o utilizador fornece um número negativo.
O seu programa deve possibilitar a seguinte interação:

    `Escreva um número de segundos`

    `(um número negativo para terminar)`

    `? 45`

    `O número de dias correspondente é  0.000520833333333333`

    `Escreva um número de segundos`

    `(um número negativo para terminar)`

    `? 6654441`

    `O número de dias correspondente é  77.0189930555555`

    `Escreva um número de segundos`

    `(um número negativo para terminar)`

    `? -1234`

"""

def dias():
    segundos = eval(input("Escreva um número de segundos \n(um número negativo para terminar)\n\n?"))

    while (not (segundos < 0)):
        dias = segundos / 60/60/24
        print("O número de dias correspondente é " + str(dias))

        segundos = eval(input("Número de segundo -> "))
    
dias()
