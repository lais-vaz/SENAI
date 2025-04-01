#-*- coding: UTF-8 -*-

print("digite seu peso e sua altura e eu te direi se você esta com um peso favorável")

peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))

imc = peso/altura**2

if imc <20:
    print("você esta abaixo do peso")

elif imc >20 and imc <= 25:
    print("você esta no peso normal")

elif imc >25 and imc <=30:
    print("você esta sobre o peso")

elif imc >30 and imc <=40:
    print("você esta obeso")

else:
    print("você esta obeso mórbido")
    
