import os
os.system("cls")

#ENTRADA
print("===== CARDÁPIO =====")
print("1 - Picanha ........ R$ 25,00")
print("2 - Lasanha ........ R$ 20,00")
print("3 - Strogonoff ..... R$ 18,00")
print("4 - Bife Acebolado . R$ 15,00")
print("5 - Pão com ovo .... R$ 5,00")
codigo = int(input("Digite o código do prato: "))

match codigo:
    case 1:
        print("Prato escolhido: Picanha")
        print("Valor: R$ 25,00")

    case 2:
        print("Prato escolhido: Lasanha")
        print("Valor: R$ 20,00")

    case 3:
        print("Prato escolhido: Strogonoff")
        print("Valor: R$ 18,00")

    case 4:
        print("Prato escolhido: Bife Acebolado")
        print("Valor: R$ 15,00")
    
    case 5:
        print("Prato escolhido: Pão com ovo")
        print("Valor: R$ 5,00")

    case _:
        print("Código inválido")
   
    

