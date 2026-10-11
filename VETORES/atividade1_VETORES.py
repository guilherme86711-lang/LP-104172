import os
os.system("cls")


notas = []

for i in range(3):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

media = sum(notas) / 3

print("\nNotas escolhidas:", notas)
print("Média:", media)
