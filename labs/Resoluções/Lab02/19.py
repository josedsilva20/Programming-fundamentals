"""
Escreva um programa em Python escreve o seguinte:


1 x 8 + 1 = 9
12 x 8 + 2 = 98
123 x 8 + 3 = 987
1234 x 8 + 4 = 9876
12345 x 8 + 5 = 98765
123456 x 8 + 6 = 987654
1234567 x 8 + 7 = 9876543
12345678 x 8 + 8 = 98765432
123456789 x 8 + 9 = 987654321


Os valores do primeiro termo da multiplicação e o resultado devem ser calculados pelo seu programa.

"""


def forma():
    crescente   = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    decrescente = crescente[::-1]               # Inverte a ordem do primeiro
    final       = ""
    
    for i in range (len(crescente)):
        final += str(crescente[i]) + " x 8 + " + str(i) + " = " + str(decrescente[i])
    
    return final

print(forma())