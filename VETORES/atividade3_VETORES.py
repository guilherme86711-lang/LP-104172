import os
os.system("cls")

vetor_numeros = []

vetor_negativo = []

soma = 0 

QUANTIDADE_NOTAS = 5

for i in range(QUANTIDADE_NOTAS):
    
    numeros = float(input(f"DIGITE O {i+1}º NUMERO :"))
    
    vetor_numeros.append(numeros)
    if numeros < 0:
        numero_negativo = numeros
        vetor_negativo.append(numero_negativo)
else:
    soma += numeros


    for i, numero_negativo in enumerate(vetor_negativo):
        print(f"{i+1}º numero negativo: {numero_negativo}")

    print(f"soma dos positivos: {soma}")
