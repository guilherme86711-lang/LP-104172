import os 
os.system("cls")



def valor_posi_negat(numero):
    print(f"o numero digitado é:{numero}")
    if numero > 0:
        resultado = "positivo"
    elif numero == 0:
        resultado  = "neutro"
    else: 
        resultado = "negativo"
        return resultado

numero = int(input("digite um número: "))
resultado = valor_posi_negat(numero)

print(f"o número: {numero} é {resultado}")