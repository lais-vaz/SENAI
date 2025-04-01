# -*- coding: UTF-8 -*-

L = []
soma = 0

for i in range (4):
    nota = int(input("digite as notas: "))
    L.append(i)
    soma = soma + nota

for i in L:
    print(i)

m = soma/4
print(m)
