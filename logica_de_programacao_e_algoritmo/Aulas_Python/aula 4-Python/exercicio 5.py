#-*- coding: UTF-8 -*-

def circulo():
    raio = int(input("digite o raio de um circulo: "))

    area = 3.14 * (raio ** 2)
    return area

print("o resultado é: ", circulo())
