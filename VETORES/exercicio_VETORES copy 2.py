import os
os.system("cls")

print("=  INSERINDO NÚMEROS NO VETOR  =")

vetor_numeros = []

for i in range(3):
    numeros = int(input("DIGITE UM NÚMERO: "))
    vetor_numeros.append(numeros)

print("\n = EXIBINDO NÚMEROS DO VETOR = ")

for  valor in vetor_numeros:
    print(f"valor{valor}")