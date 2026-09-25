import os
import time
os.system("cls")

#ENTRADA
numero = int(input("informe um número:"))

#PROCESSO

for i in range (numero, 0, -1):
    time.sleep(1)
    print(i)
