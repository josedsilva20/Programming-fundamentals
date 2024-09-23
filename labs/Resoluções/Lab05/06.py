""" 
Defina a função `dias_mes`
 que recebe uma cadeia de caracteres, correspondentes às 3 primeiras 
 letras (minúsculas) do nome de um mês e um ano, e tem como valor um 
 número inteiro correspondendo ao número de dias desse mês. 
 No caso de uma cadeia de caracteres inválida, a sua função deverá 
 gerar um erro de valor (*ValueError*). Use a função *bissexto* do 
 exercício anterior. A sua função deve permitir gerar a interação:

```Python
dias_mes('jan', 2017)
31

dias_mes('fev', 2016)
29

dias_mes('MAR', 2017)
ValueError: Mes nao existe
```
"""

def bissexto(ano):
    if not((ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0)):
        return False
        
    return True

def dias_mes(mes, ano):
    meses = ("jan", "fev", "mar", "abr", "mai", "jun", \
        "jul", "ago", "set", "out", "nov", "dez")
    
    if not (type(mes) == str and mes in meses):
        raise ValueError("Mês inválido.")
    
    elif not( type(ano) == int and ano >= 0):
        raise ValueError("Ano inválido.")
    
    for i in range (len(meses)):
        if (mes == meses[i]):
            if (i % 2 == 0):
                if (i > 5): 
                    return 30
                if (i <= 5):
                    return 31

            if (i == 1):
                if (bissexto(ano)):
                    return 29
                return 28
    
print(dias_mes("fev", 2024))
            
