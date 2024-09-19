"""Escreva um programa em Python que lê valores correspondentes 
a uma distância percorrida (em Km) e o tempo necessário para a 
percorrer (em minutos), e calcula a velocidade média em Km/h e m/s"""

def calcula():
    distancia = eval(input("Digite a distância em Km: "))
    tempo = eval(input("Indique o tempo: "))

    print("velocidade: " + str(distancia/tempo) + " m/s.")

calcula()