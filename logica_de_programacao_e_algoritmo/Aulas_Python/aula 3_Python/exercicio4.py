#-*- coding: UTF-8 -*-

contagem = 0

print("digite vários números, quando for digitado o núemro 0 (zero) o porgrama vai parar")

while True:
    num = int(input("digite um número: "))
    if num >=100 and num <=200:
        contagem +=1
        
    elif num == 0:
        break

print("foram contabilizados entre 100 e 200: ", contagem)
