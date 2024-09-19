from math import sqrt

"""
Escreva um programa em Python que lê cinco números reais e calcula a sua média 
e o seu desvio padrão. A média, $\bar x$, e o desvio padrão,  são dados 
respectivamente por:
"""

def media_e_desvio():
    soma = 0
    qtd = 3
    numeros = ()
    ordem = 0


    # Cálculo de média
    while (qtd > 0):
        numeros += (eval(input("Digite o número -> ")),)
        soma += numeros[ordem]
        qtd -= 1
        ordem += 1

    ordem = 0
    qtd = 3
    media = soma / qtd
    soma = 0
    


    # Cálculo de desvio padrão
    while (qtd >= 0):
        soma += (numeros[ordem] - media) ** 2
        qtd -= 1
        soma += 1
    
    desvio = sqrt((1/4) * soma)

    print("Média -> " + str(media))
    print("Desvio padrão -> " + str(desvio))

media_e_desvio()