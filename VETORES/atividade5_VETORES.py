import os
os.system("cls")

print("======CARDAPIO=========")
print("CÓDIGO     PRATO          VALOR") 
print("1        PICANHA          25,00 ")
print("2       LASANHA          20,00 ")
print("3       STROGONOFF       18,00 ")
print("4       BIFE ACEBOLADO   15,00 ")
print("5       PÃO COM OVO      5,00 ")

vetor_pratos = []
vetor_precos = []
while True:
    prato = (input("DIGITE O CODIGO DO PRATO QUE DESEJA: "))
    
    match prato:
        case 1:
            prato = 'Picanha'
            preco = 25
        case 2:
            prato = 'Lasanha'
            preco = 20
        case 3:
            prato = 'Strogonoff'
            preco = 18
        case 4:
            prato = 'Bife acebolado'
            preco = 15
        case 5:
            prato = 'Pão com ovo'
            preco = 5
        case _:
            print('Opção inválida. \nTente novamente... \n')
    if prato >= 1 and prato <= 5:
        vetor_pratos.append(prato)
        vetor_precos.append(preco)

        continuar = input("DESEJA ESCOLHER OUTRO PRATO?\nRESPONDA COM S OU N").upper()
    if continuar == "N":
        break
    os.system("cls")
    if sum(vetor_precos)== 0:
        print("NENHUM PRATO SELECIONADO.")
    else:
        print("\n===PRATOS ESCOLHIDOS===")
        for i, prato in enumerate(vetor_pratos, start=1):
            print(f"{i}º  prato {prato}")
        print(f"\n TOTAL: R$ sum{vetor_precos}")
        print("\nVOLTE SEMPRE!")
        
        