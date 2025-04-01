#-*- coding: UTF-8 -*-

print ("envie quantos cigarros são fumados por dia e há quantos anos a pessoa fuma, e direi quanto tempo de vida a menos a pessoa terá")

cigarros = int(input("quantos cigarros são fumados: "))
anos =  float(input(" a quantos anos a pessoa fuma: "))
reducao = 365*anos*cigarros*10/1440

print ("a pessoa ja perdeu %.2f dias de vida" %reducao)
