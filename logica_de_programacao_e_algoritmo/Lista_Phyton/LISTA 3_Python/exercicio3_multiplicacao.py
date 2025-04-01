#-*- coding: UTF-8 -*-

def tabuada(calculo):
    for tabuadas in range(0,11):
       print(tabuadas,"*", calculo, "=", tabuadas * calculo )
       
numero = int(input("digite um número para a tabuada: "))
tabuada (numero)


