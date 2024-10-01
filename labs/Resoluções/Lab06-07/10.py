""" 
#### 10.
Um método básico para codificar um texto corresponde a isolar os caracteres nas posições pares para um lado e os caracteres nas posições ímpares para outro, juntando depois as duas partes anteriormente obtidas. Por exemplo, o texto **abcde** é codificado por **acebd**.
* (a) Defina uma função `codifica` que codifica uma cadeia de caracteres de acordo com o algoritmo apresentado. Não é necessário validar os dados de entrada. Por exemplo,
```Python
codifica('abcde')
'acebd'
```
* (b) Defina uma função `descodifica` que descodifica uma cadeia de caracteres de acordo com o algoritmo apresentado. Não é necessário validar os dados de entrada. Por exemplo,
```Python
descodifica('acebd')
'abcde'
```
"""

def codifica(palavra):
    par     = ""
    impar   = ""
    
    for i in range(len(palavra)):
        if ((i+1) % 2 == 0):
            par += palavra[i]
        else:
            impar += palavra[i]
        
    return impar + par
    
print (codifica('abcde'))


def descodifica(palavra):
    par = ""
    impar = ""
    
    if (len(palavra) % 2 != 0):
        impar = palavra[:len(palavra) // 2]
        par = palavra[len(palavra) // 2 ::]

    else:
        impar = codifica(palavra[:(len(palavra) / 2) - 1])
        par = codifica(palavra[(len(palavra) // 2) - 1 ::])
    
    return par + impar
        
print(descodifica('acebd'))
            