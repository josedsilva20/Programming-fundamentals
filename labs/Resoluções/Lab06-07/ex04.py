""" 
#### 4.
Escreva a função `filtra_pares` que recebe um tuplo contendo algarismos, verificando a correção do seu argumento, e devolve o tuplo contendo apenas os algarismos pares. Por exemplo

```Python
filtra_pares((2, 5, 6, 7, 9, 1, 8, 8))
(2, 6, 8, 8)
```
"""

def filtra_pares(tuplo):
    res = ()
    if not isinstance(tuplo, tuple):
        raise ValueError("Not a tuple")
    
    for i in tuplo:
        if not (isinstance(i, int) and 0 <= i <= 9):
            raise ValueError("Argumento não é dígito")
        
        if (i % 2) == 0:
            res += (i,)

    return res

print(filtra_pares((2, 5, 6, 7, 9, 1, 8, 8)))