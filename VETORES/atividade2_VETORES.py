import os
os.system("cls")

notas = []

for i in range(4):
    nota = float(input(f"digte sua {i + 1 }ª nota:"))
    notas.append(nota)
    media = sum(notas)/4
if media >= 7:
    print("aprovado")
elif media >= 5:
    print("recuperação")
else:
    print("reprovado")
    
print(f"\n nota escolhida: {nota}")   
print(f"sua média foi: {media}") 
    