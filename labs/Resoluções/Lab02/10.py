"""
Escreva um programa em Python que lê um número inteiro positivo e calcula o número
obtido do número lido que apenas contém os seus dígitos impares.
Por exemplo,

    `Escreva um inteiro`

    `? 785554`

    `Resultado: 7555`

"""

<<<<<<< HEAD
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
=======
def le_impares():
    res = 0
    numero = eval(input("Escreva um dígito: "))
    mult = 1


    while (numero > 0):
        digito = numero % 10
        if (digito % 2 == 1):
            res = res + digito * mult
            mult = mult * 10
        numero = numero // 10
        
    return res

print(le_impares())
>>>>>>> 172bdd43aa473327a6e083e77e9340b3dc9af8e2

