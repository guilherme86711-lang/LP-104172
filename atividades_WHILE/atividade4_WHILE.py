import os
os.system("cls")

while True:
    login = input("LOGIN:")
    senha = int(input("SENHA: "))
    if login == "gui" and senha == 864:
        print()
        print(f"LOGIN:{login}")
        print()
        print(f"SENHA:{senha}")
        break
    else:
        print("LOGIN E SENHA INVALIDOS.")