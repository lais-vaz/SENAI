# -*- coding: UTF-8 -*-

contadora = 0
acum = 0
soma = 0

print("digite valores e no final te darei a soma e a média deles. Digita um valor negativo para sair")

while True:
    valor = float(input("digite o números: "))
    if valor <0:
        print("você escolheu sair, tchau!")
        break
    acum = acum + valor
    contadora = contadora + 1
    soma = valor + valor

    print (f"a media dos valores digitados é de: {acum/cont:.2f}")
    
    
    
