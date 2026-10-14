import os
os.system("cls")

print("=  INSERINDO NOTAS NO VETOR  =")

vetor_notas = []
QUANTIDADE_NOTAS= 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"DIGITE A {i+1}ª NOTA: "))
    vetor_notas.append(nota)
    
#SUM - SOMAR TUDO O QUE ESTÁ NO VETOR.
media = sum(vetor_notas) / QUANTIDADE_NOTAS
menor_nota = min (vetor_notas)
maior_nota =  max(vetor_notas)

if media >= 7:
    
    print("APROVADO.")
    
elif media >= 5:
    
    print("RECUPERAÇÃO.")
    
else:
    
    resultado = "REPROVADO."
    
    print("\n = EXIBINDO AS NOTAS  DO VETOR = ")

for posicao, nota  in enumerate(vetor_notas, start=1):
    print(f"{posicao}ª nota: {nota}")
    
print(f"media: {media}")
print(f"resultado: {resultado}")

print("\n = EXIBINDO A MENOR E A MAIOR NOTAS  DO VETOR = ")
print(f"menor nota: {menor_nota}")
print(f"maior nota: {maior_nota}")




