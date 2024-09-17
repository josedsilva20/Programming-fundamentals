"""
Escreva um programa em Python que lê uma quantia em Euros e calcula o número de
notas de 50 €, 20 €, 10 €, 5 € e moedas de 2 €, 1 €, 50 cêntimos, 20 cêntimos, 10 cêntimos,
5 cêntimos, 2 cêntimos e 1 cêntimo, necessário para perfazer, essa quantia, utilizando
sempre o máximo número de notas e moedas para cada quantia, da mais elevada, para a mais baixa.
"""


def notas(valor):
    nota = (50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01)
    final = ""
    aux = 0

    for i in range(len(nota)):
        if (valor >= nota[i]):
            #   Para o caso de ser um valor certo (uma nota de 50; uma nota de 20)
            if (valor % nota[i] == 0):
                final += str(valor // nota[i]) + " notas de " + str(nota[i]) + "€. "
                return final
            
            #   Para o caso de o valor não ser perfeitamente divisível
            else:
                aux = valor % nota[i]
                valor = valor // nota[i]
                final += str(valor) + " notas de " + str(nota[i]) + "€. "
                valor = aux

    return final


print(notas(eval(input("Indique um valor em € (euros): "))))
