# -*- coding: UTF-8 -*-

def transformar (grau,num):
    result = 0

    if grau == "C para F":
        result = (num * (9/5)) + 32
        return f"{result:.2f} ºf"

    elif grau == "F para C":
        result = (num - 32)*(9/5)
        return f"{result:.2f} ºc"

    else:
        return "ESCOLHA INVALIDA"

print("escolha a temperatura em Celsius e eu te darei em Fahrenheit, e vice-versa.")
grau = input("use F (Fahrenheit) e C (Celsius), C para F ou F para C: ")
num = int(input("digite qual grau você quer converter: "))

print(transformar (grau, num))





