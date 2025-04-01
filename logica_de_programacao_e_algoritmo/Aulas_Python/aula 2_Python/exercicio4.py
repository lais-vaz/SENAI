#-*- coding: UTF-8 -*-

print("Vou calcular para você o valor da casa a comprar")
casa = float(input("Qual o valor da casa?: "))
salario = float(input("digite o seu salario"))
anos = int(input( "quantos naos você quer pagar"))

prestacao = casa / (anos*12)
porcentagem_salario = salario*30/100
print 
