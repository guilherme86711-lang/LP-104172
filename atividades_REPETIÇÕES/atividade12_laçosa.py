import os
os.system("cls")

QUANTIDADE_REPETICOES = 3
par = 0
impar = 0

for i in range(QUANTIDADE_REPETICOES):
    numero = int(input("digite um número:"))
    if numero %2==0:
        par += 1
    else:
        impar += 1

print(f"\quantidade de pares: {par}")
print(f"\quantidade de impares: {impar}")