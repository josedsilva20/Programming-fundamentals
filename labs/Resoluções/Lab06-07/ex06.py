""" 
#### 6.
Escreva a função `num_para_seq_cod` que recebe um número inteiro positivo e que devolve um tuplo contendo os algarismos codificados desse número do seguinte modo: 
* (a) cada algarismo par é substituído pelo número par seguinte, entendendo-se que o número par seguinte a 8 é o 0; 
* (b) cada algarismo ímpar é substituído pelo número ímpar anterior, entendendo-se que o número ímpar anterior a 1 é o 9. 
Por exemplo,

```Python
num_para_seq_cod(1234567890)
(9, 4, 1, 6, 3, 8, 5, 0, 7, 2)
```
"""

def num_para_seq_cod(num):
    if not (isinstance(num, int) and num > 0):
        raise ValueError("Argumento inválido.")
    
    aux = ()
    res = ()
    while (num > 0):
        aux += (num % 10,)
        num = num // 10
        
    for i in aux:
        if (i % 2 == 0):
            res += ((i + 2) % 10,)
        else:
            res += (abs(i - 2) % 10,)
    
    return res

print(num_para_seq_cod(1234567890))