import os 
import time
os.system("cls")

#FAZER UM PROGRAMA QUE SOLICITE NOME, EMAIL E TELFONE. O PRGRAMA DEVE MANTER NA TELA A LOGO DO SENAI - BAHIA
lista_produtos = []
def solicitar_dados():
    for i in range(3):
        produto = input("digite o nome do produto: ")
        lista_produtos.append(produto)
        
def mostrar_dados(lista_produtos):
    for i in range (3):
        print(f"{i+1} - {lista_produtos[i]}")
    
print("=solicitando dados=")
solicitar_dados()

print("\n =exibindo dados=")
mostrar_dados(lista_produtos)