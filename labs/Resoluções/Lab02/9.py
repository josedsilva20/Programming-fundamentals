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
<<<<<<< HEAD
    potencia = 0
    expoente = 0
    soma = ()
    final = 0
    valor = eval(input("Escreva um dígito\n(-1 para terminar)\n? "))

    while (valor >= 0 and valor != -1):
        soma += (valor,)
        potencia += 1
        valor = eval(input("Escreva um dígito\n(-1 para terminar)\n? "))


    while (potencia > 0):
        potencia -= 1
        final += soma[potencia] * 10 ** expoente
        expoente += 1

    print("O número é: " + str(final))
=======
    soma = 0
    valor = 0

    while (valor >= 0 and valor != -1):
            soma = soma * 10
            soma += valor
            valor = eval(input("Escreva um dígito\n(-1 para terminar)\n? "))
    
    return "O número é: " + str(soma)
>>>>>>> 172bdd43aa473327a6e083e77e9340b3dc9af8e2


numero()