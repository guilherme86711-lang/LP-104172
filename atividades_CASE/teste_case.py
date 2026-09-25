import os
os.system("cls")

#ENTRADA

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite a operação (+, -, * ou /): ")

#PROCESSO
match operador:
    case "+":
        resultado = numero1 + numero2

    case "-":
        resultado = numero1 - numero2

    case "*":
        resultado = numero1 * numero2

    case "/":
        resultado = numero1 / numero2

    case _:
        resultado = "Operador inválido"

print("Número 1:", numero1)
print("Número 2:", numero2)
print("Operador:", operador)
print("Resultado:", resultado)

#SAIDA