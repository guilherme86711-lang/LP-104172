import os
os.system("cls")

SUAS_NOTAS = 3

for i in range(SUAS_NOTAS):
    nota = int(input(f"DIGITE SUA {i+1}ª NOTA:"))
    media = nota + SUAS_NOTAS / 3
if media>= 7:
    print(f"sua nota é: {nota}, você está aprovado.")
else:
    print(f"você está reprovado. Nota: {nota}.")