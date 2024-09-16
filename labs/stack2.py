def new():
    return 12
    
def push(x, s):
    if isinstance(x, int) and x >= 0 and isinstance(s, int):
        return int(str(s)+'12'+(''.join(str(ord(c)) for c in str(x))))
    else:
        raise ValueError('Argumento inválido (push).')
        
def pop(s):
    if isinstance(s, int) and s > 0:
        r = str(s)
        while(r[-2:]!='12'):
            r = r[:-2]
        return int(r[:-2])
    else:
        raise ValueError('Argumento inválido (pop).')

def top(s):
    if isinstance(s, int) and s > 0:
        aux = str(s)
        r = 0
        while(aux[-2:]!='12'):
            r = r*10+int(chr(int(aux[-2:])))
            aux = aux[:-2]
        return r   
    else:
        raise ValueError('Argumento inválido (top).')
        
def is_empty(s):
    if isinstance(s, int):
        return s == 12 
    else:
        raise ValueError('Argumento inválido (is_empty).')
        
def clone(s):
    if isinstance(s, int):
        return int(str(s)[:])
    else:
        raise ValueError('Argumento inválido (is_empty).')