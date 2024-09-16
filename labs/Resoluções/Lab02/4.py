"""
Escreva um programa que lê um número inteiro correspondente a 
um certo número de segundos e que escreve o número de dias, horas,
minutos e segundos correspondentes a esse número. Por exemplo,
    Escreva o número de segundos 345678
    dias: 4; horas: 0; mins: 1; segs: 18
"""

def calcula():
    segundos = eval(input("Escreva o número de segundos: "))
    mins    = segundos / 60
    horas   = mins / 60
    dias    = horas // 24
    res     = "dias: " + str(dias) + "; horas: " + str(horas) + "; mins: " \
        + str(mins) + "; segs: " + str(mins)