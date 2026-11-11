import os 
os.system("cls")

def mostrar_saudacao(nome, idade):
    print(f"{nome} tem {idade} anos")

print("==== solicitando dados=====")

nome = input(("digite seu nome: "))
idade = int(input("digite sua idade: "))


print("====exibindo dados=====")

mostrar_saudacao(nome, idade)