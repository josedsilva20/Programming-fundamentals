""" 
Defina a função `area_circulo` que recebe o valor do raio de um círculo e tem 
como valor a área do círculo. Note-se que a área do círculo cujo raio é $r$ 
é dada por $\pi r^2$. Use o valor $3.14$ para o valor de $\pi$.
"""

from math import pi

def area_circulo(raio):
    return pi * raio ** 2;

print (area_circulo(1))