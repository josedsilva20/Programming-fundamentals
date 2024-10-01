""" 
#### 3. 
Escreva a função `implode` que recebe um tuplo contendo algarismos, verificando a correção do seu argumento, e devolve o número inteiro contendo os algarismos do tuplo, pela ordem em que aparecem. Por exemplo
```Python
implode((3, 4, 0, 0, 4))
34004

implode((2, 'a', 5))
ValueError: implode: elemento não algarismo
```
Escreva duas versões da sua função, uma utilizando um ciclo `while` e outra utilizando um ciclo `for`.
"""


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


print(implode((3, 4, 0, 0, 4)))