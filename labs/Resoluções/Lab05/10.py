""" 
Considere qualquer inteiro de 3 algarismos, desde que a diferença entre o seu 
primeiro e último dígito seja superior a $1$. Seja este número $n$. 
Inverta os algarismos de $n$, obtendo $n_i$. Subtraia o maior do menor, obtendo 
$n_s$, ou seja $n_s =| n - n_i |$. Inverta os algarismos de $n_s$, obtendo $n_{s_i}$ . 
Pode verificar que $n_s + n_{s_i} = 1089$. Por exemplo, suponhamos que $n = 246$, 
então $n_i = 642$, $n_s =396$, $n_{s_i} = 693$ e $n_s+n_{s_i} = 396 + 693 = 1089.$

#### (a) 
Escreva uma função que traduza este mistério. A sua função deve garantir que o argumento é correto. Por exemplo,
```Python
misterio(246)
1089

misterio(131)
'Condições não verificadas'
```
#### (b)
Explique este mistério.
"""


def misterio(numero):
    if not (type(numero) == int 
            and 100 <= numero <= 999
            and (numero % 100 - numero % 10 >= 1)):
        return "Condições não verificadas"
    
    n_i     =   int(str(numero)[::-1])
    n_s     =   abs(numero - n_i)
    n_s_i   =   int(str(n_s)[::-1])
    
    if (n_s + n_s_i == 1089):
        return 1089
    
    return "Condições não verificadas"

print(misterio(131))
    