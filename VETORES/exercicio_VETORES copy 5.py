import os
os.system("cls")

print("=  INSERINDO NOTAS NO VETOR  =")

vetor_notas = []
QUANTIDADE_NOTAS= 2

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"DIGITE A{i+1}º NOTA: "))
    vetor_notas.append(nota)
    
#SUM - SOMAR TUDO O QUE ESTÁ NO VETOR.
media = sum(vetor_notas) / QUANTIDADE_NOTAS
print("\n = EXIBINDO AS NOTAS  DO VETOR = ")

for posicao, nota  in enumerate(vetor_notas, start=1):
    print(f"{posicao}ª nota: {nota}")
    
print(f"media: {media}")

