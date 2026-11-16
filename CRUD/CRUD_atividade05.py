import os
os.system("cls")
from datetime import date 
def verificar_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

ano_nascimento = int(input("digite seu nascimento: "))

print(f"sua idade é: {idade} anos.")