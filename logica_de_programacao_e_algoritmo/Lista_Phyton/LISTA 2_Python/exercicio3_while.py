# -*- coding: UTF-8 -*-

print("digite a idade de varias pessoas e eu te direi o tatl de pessoa com menos de 21 anos e com mais de 50, digite -99 para sair")

menores_21 = 0
maiores_50 = 0

while True:
    idade = int(input("digite a idade: "))
    if idade == -99:
        print("você escolheu sair, bye")
        break
    elif idade < 21:
        menores_21 += 1
    elif idade > 50:
        maiores_50 += 1

print("foram contabilizadas" ,menores_21, "pessoas com menos de 21 anos")
print("foram contabilizadas" ,maiores_50, "pessoas com menos de 50 anos")
    

        
