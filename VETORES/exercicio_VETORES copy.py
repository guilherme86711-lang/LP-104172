import os
os.system("cls")

print("=  INSERINDO NÚMEROS NO VETOR  =")

vetor_numeros = []

for i in range(3):
    numeros = int(input("DIGITE UM NÚMERO: "))
    vetor_numeros.append(numeros)

print("\n = EXIBINDO NÚMEROS DO VETOR = ")

for i in range(3):
    print(f"valores:{vetor_numeros[i]}")#O I PODE SUBSTITUIR POR INDEX NAO VAI FAZER DIFERENÇA

#FAZER O VETOR MOSTRAR O ULTIMO NÚMERO PULANDO O SEGUNDO
