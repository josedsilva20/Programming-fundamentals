""" 
Escreva a função `bissexto` que recebe um número inteiro correspondente a um ano
e que devolve `True` se o ano for bissexto e `False` em caso contrário.

Um ano é bissexto se for divisível por 4 e não for divisível por 100, a não ser 
que seja também divisível por 400. Por exemplo, 1984 é bissexto, 1100 não é, e 
2000 é bissexto.

```Python
bissexto(1984)
True

bissexto(1985)
False

bissexto(2000)
True
```
"""

def bissexto(ano):
    if not((ano % 4 == 0 and ano % 100 != 0) or 
           (ano % 100 == 0 and ano % 400 == 0)):
        return False
        
    return True

print (bissexto(2000))