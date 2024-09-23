""" 
Escreva a função `serie_geom` que recebe um inteiro r e um inteiro não negativo n, e 
devolve a soma dos primeiros n+1 termos da série geométrica
$1 + r + r^2 + r^3 +\ldots + r^n$ $\left(\text{i.e., }\displaystyle\sum_{i=0}^{n}r^i\right)$. 
Por exemplo,

```Python
serie_geom(2, 4)
31

serie_geom(100, 0)
1

serie_geom(100, -1)
ValueError: serie_geom: argumento incorrecto
```
"""

def serie_geom(r, n):
    if not (type(r) == int and type(n) == int and n >= 0):
        raise ValueError("serie_geom: argumento incorrecto")
    
    soma = 1
    
    for i in range (1, n + 1):
        soma += (r ** i)
    
    return soma

print (serie_geom(100, -1))