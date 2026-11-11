import os 
import time
os.system("cls")

#FAZER UM PROGRAMA QUE SOLICITE NOME, EMAIL E TELFONE. O PRGRAMA DEVE MANTER NA TELA A LOGO DO SENAI - BAHIA
def logo_senai():
    os.system("cls")
    print("\n=========")
    print("SENAI- BAHIA")
    print("===========")

def mostrar_dados (nome, email, telefone):
        print(f"seu nome {nome}, seu email cadastrado {email}, seu telefone{telefone}")
    
print("\n=solicitando dados=")
logo_senai()

nome = input(("digite seu nome: "))
logo_senai()

email = input(("digite seu email: "))

logo_senai()
telefone = int(input("digite seu telefone: "))

logo_senai()
print("\n=dados salvos=")
mostrar_dados(nome, email, telefone)
os.system("cls")

def cadastro_login(email, telefone):
    print(f"seu email: {email}, seu telefone: {telefone}.")


print("=solicitando dados=\n 1- cadastrar cliente\n 2- mostrar dados do cliente\n 3- sair\n")
login = input("digite o que deseja fazer: ")
match login:
    case "1":
        print("==cadastrando==")
        logo_senai()
        email = input("digite seu email: ")
        telefone = int(input("digite seu telefone: "))
        os.system("cls")
        print("=cadastro concluido=")
        logo_senai()
        print(f"{email}\n {telefone}")
    case "2":
        print("==informações do cliente==")
        logo_senai()
        print(f"nome: {nome} seu email: {email}, seu telefone: {telefone}")
    case "3":
        print("==saindo==")
        time.sleep(2)
        os.system("cls")
        exit()
    case _:
        print("informações erradas")
    
    