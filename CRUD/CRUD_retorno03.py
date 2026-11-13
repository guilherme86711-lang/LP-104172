import os 
os.system("cls")

def calcular_media(nota1, nota2):
    calculo = nota1 + nota2
    media = (nota1 + nota2) / 2
    return media

def verificar_resultado(media):
    if media > 7:
        print("aprovado")
    else:
        print("reprovado.")
    return media
    
print("== solicitando notas==")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

media = calcular_media(nota1, nota2)
situacao = verificar_resultado(media)

print("== exibindo notas==")

print(f"media: {media}")
print(f"resultado: {situacao}")
