#-*- coding: UTF-8 -*-

print("digite dois valores e eu te direi na ordem crescente")

valor1 = int(input("digite o primeiro valor"))
valor2 = int(input("digite o segundo valor"))

if valor1 < valor2:
    a = valor1
    b = valor2
    print(f"O valor de A é {a} e o valor de B é {b}")

else:
    a = valor2
    b = valor1
    print(f"O valor de A é {a} e o valor de B é {b}")

