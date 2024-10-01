"""
#### 5.
Recorrendo às funções `explode`, `implode` e `filtra_pares`, defina a função `algarismos_pares` que recebe um inteiro e devolve o inteiro que apenas contém os algarismos pares do número original. Por exemplo,

```Python
algarismos_pares(6643399766641)
6646664
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

def implode(tuplo):
    res = 0
        
    if not isinstance(tuplo, tuple):
        raise ValueError("Não é tuplo")
    
    for i in (tuplo):
        if not isinstance(i, int):
            raise ValueError("Não tem todos elementos como algarismos")
        
        else:
            res = res * 10 + i
            
    return res


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


def algarismos_pares(num):
    res = filtra_pares(implode(explode(num)))
    
    return explode(res)

print(algarismos_pares(6643399766641))