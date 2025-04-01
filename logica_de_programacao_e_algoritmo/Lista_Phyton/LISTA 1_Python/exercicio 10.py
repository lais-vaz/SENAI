#-*- coding: UTF-8 -*-

print("digite três valores reais e eu te direi se pode ser formado um triângulo e qual seria")

valor1 = float(input("digite o primeiro valor: "))
valor2 = float(input("digite o segundo valor: "))
valor3 = float(input("digite o terceiro valor"))

if valor1 + valor2 < valor3 or valor1 + valor3 < valor2 or valor2 +valor3 < valor1:
    print("erro")

elif valor1 == valor2 and valor1 == valor3 and valor2 == valor3:
    print("triangulo equilatero")

elif valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
    print("triangulo escaleno")

else:
    print("triangulo isosceles")
