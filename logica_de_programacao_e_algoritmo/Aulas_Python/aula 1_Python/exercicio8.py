#-*- coding: UTF-8 -*-

print("envie a quantidade em km percorrida com seu carro alugado e por quantos dias")

km = float(input("Quantos km você percorreu: "))
dias = int(input("por quantos dias você alugou: "))
preco = km*0.15+dias*60

print ("você deverá pagar R$%.2f pelo carro alugado" %preco)
