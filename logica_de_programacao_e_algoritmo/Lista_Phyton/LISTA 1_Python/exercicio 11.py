#-*- coding: UTF-8 -*-

print("digite qual a sua nota que eu te direi se você esta aprovado, de recuperação ou reprovado")

nota = int(input("digite sua nota"))

if nota <3:
    print("você esta reprovado")

elif nota >=7:
    print("você esta aprovado")

elif nota >3 <7:
    print("você esta de recuperação")

