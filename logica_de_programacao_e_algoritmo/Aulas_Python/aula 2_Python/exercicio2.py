#-*- coding: UTF-8 -*-

print ("Digita seu salário e eu te darei o valor do aumento")

salario = float(input("digite seu salário: "))

if salario > 1250:
    aumento = salario / 100 * 10

else:
    aumento = salario /100 * 15

print("o seu novo salario é: ",aumento)
