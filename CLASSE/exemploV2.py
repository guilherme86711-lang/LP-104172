from dataclasses import dataclass
import os

os.system("cls")


@dataclass
class Cliente:
    nome: str
    telefone: int
    email: str


def mostrar_dados(self):
    print(f"nome: {self.nome}")
    print(f"telefone: {self.telefone}")
    print(f"email: {self.email}")
    print("="*30)
    
    
def email_marketing(self):
    print(f"nome: {self.nome}")
    print(f"telefone: {self.telefone}")
    print(f"email: {self.email}")
    print("="*30)

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
    cliente.mostrar_dados()
    
    
for cliente in lista_cliente:
    cliente.email_marketing()