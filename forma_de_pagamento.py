import os
os.system("cls")

#ENTRADA

produto = float(input("digite o valor do produto: "))
pagamento = (input("digite a forma de pagamento: "))



#PROCESSO

match pagamento:
    case "pagamento à vista":
        desconto = produto * 0.10
        total = produto - desconto
        print(f"valor do produto: {produto}")
        print(f"valor do desconto: {desconto}")
        print(f"valor total: {total}")

    case "pagamento à prazo":
        parcela = int(input("digite a quantidade de parcelas:"))
        valor_parcela = produto / parcela
        print(f"valor do produto: {produto}")
        print(f"quantidade de parcela: {parcela}")
        print(f"valor de cada parcela: {valor_parcela}")
        print(f"total a pagar: {produto}")
        