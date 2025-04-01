# -*- coding: UTF-8 -*-

print("digite seu salário e quantos porcentos você quer de aumento")

salario = float(input("digite seu salário"))
porcentagem = int(input("digite a porcentagem"))

total = salario * (porcentagem/100) 
diferenca_do_salario = total + salario

print("o total do salário novo é: ", total)
print("e a diferença é de: ", diferenca_do_salario)

