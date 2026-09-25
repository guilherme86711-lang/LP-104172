import os
os.system("cls")

#ENTRADA
soma = 0
for i in range(5):
    numero = int(input(f"digite o {i+1}º numero:"))
    soma = (numero + soma)

print("o resultado da soma de todos os números é:", soma)