#-*- coding: UTF-8 -*-

print("Digite dois números e eu irei efetuar a adição, caso for maior que 20 irei adicionar 8, se for menor que 20 irei subtrair 5")
num1 = int(input("digite o primeiro numero"))
num2 = int(input("digite o segundo numero"))

soma = num1 + num2

if soma >20:
    valor = soma + 8

else:
    valor = soma - 5

print ("o resultado dos dois números foi: ", valor)
