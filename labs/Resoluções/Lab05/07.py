from math import log

""" 
Quando se efectua um depósito a prazo de uma quantia $q$ com uma taxa
de juros $j$ $(0 < j < 1)$, o valor do depósito ao fim de $n$ anos é dado por:
$$q\times(1+j)^n$$
#### (a)
Escreva a função `valor` que recebe como argumentos um número inteiro 
positivo $q$ correspondente à quantia depositada, um decimal $j$ no intervalo 
$]0,1[$ correspondente à taxa de juros e um inteiro positivo $n$ correspondente 
ao número de anos que o dinheiro está a render, e, verificando a correcção dos 
argumentos, devolve um decimal correspondente ao valor do depósito ao fim desse 
número de anos. Caso os argumentos não estejam correctos, deverá gerar um erro. 
Por exemplo,

```Python
valor(100, 0.03, 4)
112.55088100000002
```

b)

Usando a função da alínea anterior, escreva uma função que calcula 
ao fim de quantos anos consegue duplicar o seu dinheiro. 
Não é necessário validar os dados de entrada. Por exemplo,
```Python
duplicar(100, 0.03)
24
```
Suponha que não é permitido utilizar um ciclo para resolver esta questão. 
Conseguiria resolvê-la?
"""


def valor(quantia, juro, anos):
    if not (type(quantia) == int and type(juro) == float and type(anos) == int):
        raise TypeError("Tipos de argumentos inválidos.")
    
    elif not (quantia > 0 and 0 < juro < 1 and anos > 0):
        raise ValueError("Argumentos invalidos.")
    
    return quantia * (1 + juro) ** anos

print (valor(100, 0.03, 4))


def duplicar(quantia, juro):
    return round(log(2, 1 +juro))
    
print (duplicar(100, 0.03))