#-*- coding: UTF-8 -*-

num = int(input("digite um numero para a contagem regressiva: "))

def contadora(num):

    for contagem in range(num, 0, -1):
        print(contagem)
contadora(num)
print ("feliz aniversario!!")

