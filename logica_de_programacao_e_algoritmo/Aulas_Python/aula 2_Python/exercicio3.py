#-*- coding: UTF-8 -*-

print("Digite dois números e qual operação você deseja realizar")
operacao = input("dgite uma das operação: +, -, * ou /: ")

num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))

if operacao == '+':
    resultado = num1 + num2

elif operacao == '-':
    resultado = num1 - num2

elif operacao == '*':
    resultado = num1 * num2

elif operacao == '/':
    resultado = num1 / num2

print("o resultado da operação é: ", resultado)


