import os 
os.system("cls")
def verificar_par_impar(numero):
    if numero %2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
        return resultado
print("==solicitando dados==")

numero = int(input("digite um número: "))
resultado = verificar_par_impar(numero)
print("\n==exibindo dados==")
print(f"o número: {numero} é {resultado} ")
resultado = verificar_par_impar(numero)

    