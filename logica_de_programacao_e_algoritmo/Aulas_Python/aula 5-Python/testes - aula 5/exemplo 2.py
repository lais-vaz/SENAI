#Cálculo da média aritmética de 5 notas de um aluno.

# -*- coding: UTF-8 -*-

notas = [6, 7, 5, 8, 9]
soma = 0
x = 0

while x < 5:
    soma += notas[x]
    x += 1

print ("Média: %5.2f" % (soma / x))
