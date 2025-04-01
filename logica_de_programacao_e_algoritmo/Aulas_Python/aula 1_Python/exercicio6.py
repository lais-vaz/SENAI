#-*- coding: UTF-8 -*-

print("envie a distância e a velocidade média da viagem e direi quanto tempo ela durará")

velocidade = float(input("dê a velocidade (km/h): "))
distancia = float(input("dê a distância (km): "))
tempo = distancia / velocidade

print("a viagem vai durar cerca de", tempo, "horas")
