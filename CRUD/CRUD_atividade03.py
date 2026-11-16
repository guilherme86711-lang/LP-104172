import os
os.system("cls")

def cm_metro(metros):
    return metros * 100
metros = float(input("digite os metros para centimetro: "))
cm = cm_metro(metros)

print(f"{metros} são {cm} centimetros.")