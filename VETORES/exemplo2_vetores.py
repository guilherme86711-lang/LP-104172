import os
os.system("cls")

vetor_nota = []

for i in range(3):
    nota = float(input("DIGITE SUA NOTA:"))
    vetor_nota .append(nota) #INSERIDO A NOTA NO VETOR DE NOTAS

for i in range(3):
    print(f"nota: {vetor_nota[i]}")