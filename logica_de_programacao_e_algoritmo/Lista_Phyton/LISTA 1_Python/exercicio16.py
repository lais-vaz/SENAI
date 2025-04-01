#-*- coding: UTF-8 -*-

print("digite sua idade e eu te direi sua faixa etária")

idade = int(input("digite sua idade: "))

if idade <=2:
    print ("a pessoa é um bebê")

elif idade >2 and idade <=12:
    print ("a pessoa é uma criança")

elif idade >12 and idade <=23:
    print ("a pessoa é um adolescente")

elif idade >23 and idade <=70:
    print("a pessoa é um adulto")

else:
    print("a pessoa é um idoso")
