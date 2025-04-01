#-*- coding: UTF-8 -*-

contagem = 0

print("envie números e eu contarei eles, digite um negativo para parar o programa")

while True:
    usua = int(input("digite um número: "))
    if usua <0:
        break
    else:
        contagem += 1

print("o resultado da contagem é: ",contagem)
