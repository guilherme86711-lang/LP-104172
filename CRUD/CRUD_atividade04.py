import os
os.system("cls")

def inflacao(preco):
    if preco < 100:
        preco = preco + (preco*1)
    else:
        preco = preco+(preco*1)
        return preco
preco = float(input("digite o preço do produto:  $"))

print(f"preço total: ${inflacao(preco)}")

