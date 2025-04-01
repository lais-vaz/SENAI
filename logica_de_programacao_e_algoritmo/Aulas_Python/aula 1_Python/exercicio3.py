# -*- coding: UTF-8 -*-

print("digite a quantidade de dias, horas, minutos e segundos, que eu lhe darei o total em segundos")

dias = int(input("digite os dias"))
horas = int(input("digite as horas"))
minutos = int(input("digite os minutos"))
segundos = int(input("digite os segundos"))

cdias = ((dias * 24)* 60)* 60
choras = (horas * 60)*60
cminutos = (minutos * 60)

total = cdias + choras + cminutos + segundos

print("o valor em segundo é: ",total)
