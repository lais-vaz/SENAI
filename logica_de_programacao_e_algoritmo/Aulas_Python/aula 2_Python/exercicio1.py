#-*- coding: UTF-8 -*-

print ("Qual a velocidade do seu carro?")

velocidade = float(input("digite a velocidadedo seu carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print ("utrapassou a velocidade, você foi multado", multa)

else:
    print("Esta dentro da velocidade")
