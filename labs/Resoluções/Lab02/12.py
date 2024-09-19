def soma():
    x       = eval(input("Qual o valor de x\n?"))
    n       = eval(input("Qual o valor de n\n?"))
    soma    = 1
    termo  = 1
    i       = 1
    
    while (i <= n):
        termo = termo * (x / i)
        soma += termo
        i += 1
    
    return "O valor da soma é: " + str(soma)

print(soma())