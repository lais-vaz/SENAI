#-*- coding: UTF-8 -*-

def nummaior():
    num1 = int(input("digite um valor"))
    num2 = int(input("digite um valor"))
    if num1 > num2:
        return num1
    else:
        return num2

print ("o maior numero é: ", nummaior())
