# -*- coding: UTF-8 -*-

print("digite o preço de sua mercadoria e o percentual de desconto")

mercadoria = float(input("digite o valor da sua mercadoria"))
percentual = int(input("digite o percentual de desconto"))

valor_desconto = mercadoria * percentual/100
total = mercadoria - valor_desconto

print("o total do desconto é: ", valor_desconto)
print("o valor total é: ", total)                  
