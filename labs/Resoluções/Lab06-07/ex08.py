""" 
#### 8.
Defina a função `junta_ordenados` que recebe dois tuplos contendo inteiros, ordenados por ordem crescente. 
e devolve um tuplo também ordenado com os elementos dos dois tuplos. Por exemplo,

```Python
junta_ordenados((2, 34, 200, 210), (1, 23))
(1, 2, 23, 34, 200, 210)
```
"""



def junta_ordenados(t1, t2):

    i1 = 0 
    i2 = 0
    res = ()
    
    while (i1 < len(t1) or i2 < len(t2)):
        if (i2 >= len(t2) or t1[i1] < t2[i2]):
            res += (t1[i1],)
            i1 += 1
        else:
            res += (t2[i2],)
            i2 += 1
    return res 
    
    
print (junta_ordenados((2, 34, 200, 210), (1, 23)))