# -*- coding: UTF-8 -*-

print("digite números e eu te direi qual é o mairo e qual é o menor, digite um número negativo para sair")

valor = float(input("digite um valor: "))

maior_valor = valor
menor_valor = valor

while valor > 0:
    valor = float(input("digite um valor: "))
    if valor <0:
        break
    elif valor > maior_valor:
        maior_valor = valor

    elif valor < menor_valor:
        menor_valor = valor

print("maior valor é: ", maior_valor)
print("menor valor é: ", menor_valor)
