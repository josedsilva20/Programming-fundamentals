"""
Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.
"""

def soma_digitos(numero):
    soma = 0

    while (numero >= 1):
        soma += numero % 10
        numero = numero // 10
    
    return soma

print(soma_digitos(int(input("Indique um inteiro -> "))))
