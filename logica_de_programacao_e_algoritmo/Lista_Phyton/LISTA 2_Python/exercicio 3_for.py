#-*- coding: UTF-8 -*-

print("apresentarei  o fatorial de um número a sua escolha")
num = int(input("digite um número para apresentar o seu faotrial: "))
fatorial = 1

for i in range (1, num +1):
    fatorial = i * fatorial
print ("o resultado da fatorial é: ", fatorial)
