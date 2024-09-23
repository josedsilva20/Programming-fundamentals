""" 
Utilizando a função *area_circulo* do exercício anterior, escreva a função `area_coroa`
que recebe dois argumentos, $r1$ e $r2$, e tem como valor a área da coroa circular de 
raio interior $r1$ e raio exterior $r2$. 
A sua função deverá gerar um erro de valor (*ValueError*) se o valor de $r1$ for maior que o valor de $r2$.
"""

from math import pi

def area_circulo(raio):
    return pi * raio ** 2;

def area_coroa(r1, r2):
    if (r1 > r2):
        raise ValueError("Raio interior não pode ser maior que exterior")
    
    return "Raio de r1: " + str(area_circulo(r1)) + " e r2: " + str(area_circulo(r2))

print (area_coroa(2, 2))