#-*- coding: UTF-8 -*-

print("digite a temperatura e eu te direi como esta o clima")

temperatura =  int(input("digite a temperatura"))

if temperatura <=15:
    print("está muito frio")

elif temperatura >=16 and temperatura <=23:
    print ("está frio")

elif temperatura >23 and temperatura <=26:
    print("está agradável")

elif temperatura >26 and temperatura <=30:
    print ("está calor")

else:
    print("está muito quente")
    
