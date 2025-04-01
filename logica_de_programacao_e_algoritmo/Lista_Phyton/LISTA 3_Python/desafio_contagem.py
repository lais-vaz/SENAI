# -*- coding: UTF-8 -*-

numero = int(input("digite umnumero e eu te direi quantos digitos tem: "))

def digitos (num):
    cont = 0
    while num >= 1:
        num = num/10
        cont+= 1
    return cont

print(f"seu numero tem {digitos (numero)} digitos")
