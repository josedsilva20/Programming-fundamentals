""" 
#### 2.
Escreva a função `explode` que recebe um número inteiro positivo, verificando a correção do seu argumento, 
e devolve o tuplo contendo os dígitos desse número, pela ordem em que aparecem no número. Por exemplo

```Python
explode(34500)
(3, 4, 5, 0, 0)

explode(3.5)
ValueError: explode: argumento não inteiro positivo
```
"""

def explode(num):
    if not (isinstance(num, int) and num >= 0):
        raise ValueError("explode: argumento não inteiro positivo")
    
    res = ()
    
    while (num > 0):
        res += (num % 10,)
        num = num // 10
        
    final = res[::-1]
    
    return final

print(explode(34500))