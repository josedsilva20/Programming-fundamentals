""" 
Defina a função `horas_dias` que recebe um inteiro correspondente a um certo
número de horas e que tem como valor um número decimal que traduz o número 
de dias correspondentes ao seu argumento. Por exemplo:

    horas_dias(48)
    2.0

    horas_dias(10)
    0.4166666666666667

"""

def horas_dias(horas):
    return float(horas / 24);

print (horas_dias(25))