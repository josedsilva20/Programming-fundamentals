"""Escreva um programa em Python que pede ao utilizador que lhe forneça 
dois números (x e y) e que escreve o valor de (x+3*y)*(x-y). 
O seu programa deve gerar uma interação como a seguinte:

    Vou pedir-lhe dois numeros
    Escreva o primeiro numero, x = 5
    Escreva o segundo numero, y = 6
    O valor de (x+3*y)*(x-y) é: -23 """

def conta():
    print("Vou pedir-lhe dois numeros")
    x = eval(input("Escreva o primeiro numero, x = "))
    y = eval(input("Escreva o segundo numero, y = "))

    res = (x+3*y)*(x-y)

    print("O valor de (" + str(x) + "+3*" + str(y) + ")*(" + str(x) + "-" + str(y) + ") é:" + str(res))

conta()
