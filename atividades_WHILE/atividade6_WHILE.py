import os
os.system("cls")

soma = 0
QUANTI_TENTATIVA = 3
for i in range(QUANTI_TENTATIVA):
    while True:
        nota = int(input("DIGITE SUA NOTA:"))
        if nota < 0 or nota > 10:
            input("DIGITE SUA NOTA NOVAMENTE:")
            os.system("cls")
        else:
            soma += nota
            break
media = soma / QUANTI_TENTATIVA
if media < 5:
    print(f"media {media}: voce esta reprovado.")
elif media >= 5 and media <= 6.9:
    print(f"media {media}: voce esta em recuperação ")
else:
    print(f"media {media}: aprovado.")
        
