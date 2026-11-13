import os 
os.system("cls")

def calcular_notas(nota1, nota2):
    calculo = nota1 + nota2
    resultado = nota1 + nota2
    return resultado


print("== solicitando notas==")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

soma = calcular_notas(nota1, nota2)

print("== exibindo notas==")

print(f"soma: {soma}")
    