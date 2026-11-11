import os 
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



