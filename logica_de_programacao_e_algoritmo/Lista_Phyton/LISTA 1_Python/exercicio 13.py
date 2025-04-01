#-*- coding: UTF-8 -*-

print("digite sua nota e o número de faltas e eu te direi qual é a sua situação")

nota1 = float(input("digite sua nota"))
nota2 = float(input("digite sua nota"))
nota3 = float(input("digite sua nota"))
falta = int(input("digite o número de faltas"))

falta_max = 80 * 25 / 100

media = (nota1 + nota2 + nota3) / 3


if falta > falta_max:
    print("você repetiu por falta")

elif media <7 and media >=0:
    print("você foi reprovado")

elif media >=7 and media <=10:
    print("você foi aprovado")

else:
    print("invalido")



