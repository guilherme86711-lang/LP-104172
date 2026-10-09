import os
os.system("cls")

print("====CADASTRO DE LOGIN=====")

login = (input("\nCADASTRE SEU LOGIN: "))

senha = int(input("\nCADASTRE SUA SENHA: "))

tentativa = 0

limite_tentativa = 3
os.system("cls")
while tentativa < limite_tentativa:

    login_salvo = (input("DIGITE SEU LOGIN CADASTRADO: "))
    senha_salva = int(input("DIGITE SUA SENHA CADASTRADA:"))
    if login_salvo == login and senha_salva == senha:
        print("===LOGIN CONCLUÍDO=====")
        break
    else:
        tentativa += 1
        limite_restantes = limite_tentativa - tentativa
        if limite_restantes > 0:
            input(f"===login inválido ==\n você tem {limite_restantes} tentativas \n\n tente novamente \n")
        else:
            print("\nACESSO BLOQUEADO. \nVOCê NAO POSSUI MAIS TENTATIVAS.")
            break
        os.system('cls')