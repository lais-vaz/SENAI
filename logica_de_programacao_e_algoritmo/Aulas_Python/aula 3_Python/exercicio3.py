#-*- coding: UTF-8 -*-

contagem = 0
soma = 0

print("envie números e eu te direi a média deles, digite um número negativo para parar o programa")

while True: 
    usua = int(input("digite um número: "))
    if usua >=0:
        contagem +=1
        soma += usua
    else:
        break
media = soma/contagem 
print ("a média é: ", media)
