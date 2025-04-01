#-*- coding: UTF-8 -*-


def cilindro():
    raio = int(input("digite o raio de um cilindro: "))
    altura = int(input("digite a altura de um cilindro: "))

    volume = 3.14 * (raio ** 2) * (altura)
    return volume

print("o resultado é: ", cilindro())
