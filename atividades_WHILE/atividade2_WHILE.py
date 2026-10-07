import os

os.system("cls")

#PROCESSO
nota = 0
soma = 0
while True:
    nota = float(input("DIGITE UMA NOTA:"))
    soma+= nota
    media = soma / 2
    escolha = (input("DESEJA ADICIONAR MAIS UMA NOTA? S/N:")).lower()
    if escolha == "n":
        break
    else:
        media = soma / 2

print(f"sua média é:{media}")