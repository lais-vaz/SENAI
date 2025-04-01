#-*- coding: UTF-8 -*-

print("digite o salario bruto e o valor da prestação e eu te direi se você pode fazer o emprestimo")

salario_bruto = float(input("digite o salario bruto"))
prestacao = float(input("digite a prestação"))

salario_porcentagem = salario_bruto * 30 / 100

if prestacao < salario_porcentagem:
    print ("você pode fazer seu emprestimo")

else:
    print("você não pode fazer o seu emprestimo")
