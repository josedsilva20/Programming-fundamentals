"""
Escreva um programa que lê um número e cria uma capicua cuja primeira metade é o número lido.
Por exemplo:

        `Escreva um número`

        `-> 347`

        `347743`

"""

def capicua(numero):
    valores = ()
    res = ()
    final = 0
    potencia = 0 


    while (numero >= 1):
        valores += (numero % 10,)
        numero = numero // 10
        potencia += 1


    res = valores[::-1]                         # Inverte o tuplo 

    res += valores                              # Cria novo tuplo com a sequencia inicial e a invertida

    potencia = potencia * 2 - 1                 # Para incluir a posicao 0

    
    for i in range (len(res)):
        final += res[i] * 10 ** potencia 
        potencia -= 1
    
    return final

print(capicua(int(input("Escreva um número: \n-> "))))



#   De forma mais fácil (sem tuplos)

def capicua_2():
    numero = eval(input("Escreva um inteiro positivo: "))
    numero_copia = numero
    copia = 0

    # Obter o inverso
    while (numero > 0):
        numero_copia = numero_copia * 10 + numero % 10
        numero = numero // 10



    return numero_copia



print(capicua_2())



