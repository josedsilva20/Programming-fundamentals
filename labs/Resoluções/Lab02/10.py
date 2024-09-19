"""
Escreva um programa em Python que lê um número inteiro positivo e calcula o número
obtido do número lido que apenas contém os seus dígitos impares.
Por exemplo,

    `Escreva um inteiro`

    `? 785554`

    `Resultado: 7555`

"""

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

