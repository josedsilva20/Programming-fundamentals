"""
Dado um conjunto de $n$ inteiros representando notas de alunos, escreva um programa 
em Python para determinar quantos tiveram nota positiva. 
Modifique o seu programa de modo a também calcular qual a percentagem de notas positivas.
"""

def positivas():
    positivas = ()

    nota = eval(input("Digite a nota: "))

    while (nota != -1):
        if (nota >= 10):
            positivas += (nota,)
        nota = eval(input("Digite a nota: "))
    
    if (len(positivas) == 0):
        print ("Não há positivas a mostrar. Máu aproveitamento")
    
    else:
        maior = positivas[0]
        for i in range (len(positivas)):
            if (positivas[i] > maior):
                maior = positivas[i]
    
    return maior


print(positivas())