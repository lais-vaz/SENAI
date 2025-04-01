#-*- coding: UTF-8 -*-

print("me diga quantas horas você trabalha e eu te direi o seu salário")

horas_trabalha = float(input("digite quantas horas você trabalha: "))

salario = horas_trabalha * 19.50

if horas_trabalha > 1500:
    novo_salario = salario - salario * 10/ 100
    print("seu salario novo é: ", novo_salario)

else:
    print("seu salario é: ", salario)
