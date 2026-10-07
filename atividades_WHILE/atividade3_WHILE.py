import os
os.system("cls")

#OLHAR A OUTRA ALTERNATIVA NA GALERIA

print(input("opção 1:  lagosta- 25,00$"))
print(input("opção 2: brownie- 10,00$"))
print(input("opção 3: coca-cola- 5,00$"))
print(input("opção 4: biscoito- 3,00$"))
print(input("opção 5: manteiga- 15,00$"))

while True:
    opcao = (input("DIGITE UMA OPÇÃO QUE DESEJA: "))
    if opcao == "opção 1":
        print()
        print("opção 1:  lagosta- 25,00$")
        break
    elif opcao == "opção 2":
        print()
        print("opção 2: brownie- 10,00$")
        break
    elif opcao == "opção 3":
        print()
        print("opção 3: coca-cola- 5,00$")
        break
    elif opcao == "opção 4":
        print()
        print("oppção 4: biscoito- 3,00$")
        break
    elif opcao == "opção 5":
        print()
        print("opção 5: manteiga- 15,00$")
        break
    else:
        print("opção fora do cardapio.")

print("FIM ALGORITMO.")        
