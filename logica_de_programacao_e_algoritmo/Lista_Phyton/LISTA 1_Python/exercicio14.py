#-*- coding: UTF-8 -*-

print("digite o valor da compra e eu te direi o valor com o lucro ")

valor_compra = float(input("digite o valor da compra:"))

if valor_compra <20:
    novo_valor = valor_compra + valor_compra * 45 / 100
    print("novo valor é: ", novo_valor)


else:
     novo_valor = valor_compra + valor_compra * 30 / 100
     print("novo valor é: ",novo_valor)
