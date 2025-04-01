#-*- coding: UTF-8 -*-

contagem = 0

print ("enviei sexos de pessoas e eu te direi quantos homens tem")

quantidade = int(input("quantos pessoas você quer enviar: "))

for i in range(quantidade):
    sexo = input("qual o sexo da pessoa F(para mulher) M(para homem): ")
    if sexo == 'M' or sexo == 'm':
        contagem +=1

print("foram contabilizados sexos homens: ", contagem)
