import os
os.system("cls")

while True:
    nota = float(input("digite uma nota entre 0 e 10:"))
    if nota < 0 or nota> 10:
        print("nota INVALIDA.")
        print("TENTE NOVAMENTE.")
    else:
        print(f"nota: {nota}")