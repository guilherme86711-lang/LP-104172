from dataclasses import dataclass
import os

os.system("cls")


@dataclass
class Cliente:
    nome: str
    telefone: int
    email: str


lista_cliente = []

print("==SOLICITANDO DADOS==")
for i in range(3):
    cad_cliente = Cliente(
        nome=input("digite seu nome: "),
        telefone=int(input("digite o tell para contato: ")),
        email = input("digite seu email: ")
    )
    lista_cliente.append(cad_cliente)
print("==EXIBINDO DADOS==")
for cliente in lista_cliente:
        print(f"nome: {cliente.nome}")
        print(f"altura: {cliente.telefone}")
        print(f"email: {cliente.email}")
        print("="*15)