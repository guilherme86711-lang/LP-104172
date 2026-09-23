import os
os.system("cls")

idade = int(input("digite sua idade: "))

#logica
if 16 > idade:
    print("voce nao pode votar.")
elif idade == 16 or idade == 17 or idade >= 65:
    print("voce pode votar, mas não é obrigatorio.")
else:
    print("voce tem que votar.")