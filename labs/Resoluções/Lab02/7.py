"""
Escreva um programa em Python que lê o número de horas, que um empregado 
trabalhou numa dada semana e o seu salário/hora e calcula o ordenado semanal
tendo em conta as horas extraordinárias. O salário é calculado do seguinte modo:
    
    se o número de horas não exceder 40, então o salário é dado pelo produto do 
    número de horas pelo salário/hora. As horas que excedem as 40 são 
    pagas a dobrar.

"""

def pagamento(horas, racio):

    if (horas <= 40):
        return horas * racio
    
    return 40 * racio + (horas - 40) * 2 *racio


horas_de_trabalho = eval(input("Insira as horas -> "))
racio = eval(input("Quanto recebe? -> "))

print("O seu salário é: " + str(pagamento(horas_de_trabalho, racio)))
