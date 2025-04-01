#-*- coding: UTF-8 -*-

print("apresentaremos a divisão de um número")
num = int(input("digite um número para apresentar os divisiveis: "))

for i in range (1, num +1):
    if num % i == 0:
        print ("os números é: ", i)
