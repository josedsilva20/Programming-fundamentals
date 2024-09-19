"""
Escreva um programa em Python que lê um número inteiro positivo e calcula o número
obtido do número lido que apenas contém os seus dígitos impares.
Por exemplo,

    `Escreva um inteiro`

    `? 785554`

    `Resultado: 7555`

"""

def le_impares(numero):
    elements = ()

    while (numero >= 1):
        if ((numero % 10) % 2 != 0):
            elements += (numero % 10,)
        numero = numero // 10

    size_elements = len(elements)
    res = 0

    for i in range (size_elements):
        res += elements[i] * 10 ** i

    return res




print(le_impares(eval(input("Digite o número: "))))

