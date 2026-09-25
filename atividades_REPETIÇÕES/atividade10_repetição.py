import os
os.system("cls")

print("acumulando VALORES em uma variável.")

soma = 0

print(f"valor INICIAL de da variável: {soma}")

for i in range(3):
    numero = int(input("\nDIgite um número para realizar a SOMA:"))

    soma = numero + soma

    print(f"valor TEMPORÁRIO da variável: {soma}")

print(f"\nvalor FINAL da variável soma: {soma}")