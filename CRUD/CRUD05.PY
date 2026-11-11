import os
os.system("cls")

def mostrar_tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i }")
print("=solicitando dados=")
numero = int(input("digite um número para tabuada: "))

mostrar_tabuada(numero)

print("\n =exibindo dados=")
mostrar_tabuada(numero)