# -*- coding: UTF-8 -*-

print("digite varios números inteiros positivos e eu te darei a soma dos números pares e números impares, digite um número maior que 1000 para sair")

numero_par = 0 
numero_impar = 0

while True:
    numero = int(input("digite números: "))
    if numero >1000:
        break
    
    elif numero %2 == 0:
        numero_par += numero

    elif numero %2 != 0:
        numero_impar += numero

print ("a soma dos números pares é: ", numero_par)
print("a soma dos números impares é: ", numero_impar)
