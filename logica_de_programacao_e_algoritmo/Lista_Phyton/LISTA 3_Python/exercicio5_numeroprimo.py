# -*- cod: UTF-8 -*-

print("digite um número e eu te direi se ele é primo")

def primo(x):
    cont = 0
    for i in range(1, x):
        if x%i==0:
            cont+=1
    if cont == 1:
        return f"{x} é primo"
    else:
        return f"{x} Não é primo"

num = int(input("digite um número: "))
print (primo(num))
