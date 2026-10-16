import os
os.system("cls")

vetor_numeros = []
QUANTIDADE_NUMEROS = 5

for i in range( QUANTIDADE_NUMEROS):
    numeros = float(input(f"DIGITE O{i+1}º NUMERO: "))
    if numeros < 0:
        numeros = 0
        vetor_numeros.append(numeros)
    else:
        vetor_numeros.append(numeros)

for i, numeros in enumerate(vetor_numeros):
    
    print(f"\n O {i+1}º VALOR.: {numeros} ")