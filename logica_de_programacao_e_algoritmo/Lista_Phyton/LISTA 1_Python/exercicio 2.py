#-*- coding: UTF-8 -*-
import math
print("digite um número, caso ele seja positivo ou igual a zero lhe darei a raiz quadrada, e o quadrado caso ele seja negativo")

num1 = float(input("digite um número: "))

if num1 >= 0:
      resultado = math.sqrt(num1)

else:
    resultado = num1**2

print("o resultado do seu número é:%.2f"%resultado)
