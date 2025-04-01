# -*- cod: UTF-8 -*-

print("Digite dois valores e uma operação ( +, -, *, /)e eu te darei o resultado")

def contadora ():
    num1 = int(input("digite o primeiro valor: "))
    num2 = int(input("digite o segundo valor: "))
    operador = input("digite uma operação: ")

    if operador == '+':
        soma = num1 + num2
        print ("você escolhei somar os valores, o resultado é: ", soma)

    elif operador == '-':
        subt = num1 - num2
        print ("você escolheu subtrair os valores, o resultado é: ", subt)

    elif operador == '*':
        mult = num1 * num2
        print ("você escolheu multiplicar, o resultado é: ", mult)

    elif operador == '/':
        divi = num1 / num2
        print ("você escolheu dividir, o resultado é: ", divi)


contadora ()


