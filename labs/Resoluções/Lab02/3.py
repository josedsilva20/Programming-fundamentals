"""
Escreva um programa em Python que pede ao utilizador que lhe forneça 
um inteiro correspondente a um número de segundos e que calcula o número
de dias correspondentes a esse número de segundos. O seu programa deve 
permitir a interação:

    Escreva um número de segundos
    ? 65432998O 
    número de dias correspondentes é 757.32636574074
    
"""

def calcula():
    segundos = eval(input("Escreva um número de segundos\n ?"))
    dias = segundos / 60 / 60 / 24
    print("número de dias correspondentes é " + str(dias))

calcula()