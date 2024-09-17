def quantas_vezes_zero():
    numero = eval(input("Digite um numero: "))
    vezes = 0

    numero_string = str(numero)
    

    for i in range(len(numero_string)):
        if (numero_string[i] == '0'):
            vezes += 1
    
    return "O zero repetiu-se " + str(vezes) + " vezes"

print(quantas_vezes_zero())
