import os
os.system("cls")

nota1 = float(input("digite o primeiro numero: "))
nota2 = float(input("digite o segundo numero: "))
nota3 = float(input("digite a nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 7:
    print("vc reprovou porra.")
elif  media >= 7:
    print("vc foi aprovado")
else:
    print("fodase")

print(media)