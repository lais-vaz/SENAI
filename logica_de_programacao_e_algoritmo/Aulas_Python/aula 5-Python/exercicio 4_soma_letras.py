# -*- coding: UTF-8 -*-

l = [ ]
soma = 0

for carac in range(10):
    letra = str(input("escreve os caracteres: "))
    l.append(letra)
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        soma = 0
        
    else:
        soma += 1
print(soma)
