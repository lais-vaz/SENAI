#-*- coding: UTF-8 -*-

cont = 0
acum = 0

while True:
    valor = float(input("digite valores e no final lhe darei a media. Digite valor negativo para sair"))
    if valor <0:
        print("você escolheu sair, tchau")
        break
    acum = acum + valor
    cont = cont +1

    #print ("a media dos valores digitados é de: % 2f"% (acum / cont))
    print(f"a media dos valores digitados é de: {acum/cont:.2f}")
