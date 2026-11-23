from dataclasses import dataclass
import os

os.system("cls")


@dataclass
class Cliente:
    nome: str
    telefone: str
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
    
    
def whatsapp_marketing(self):
    print(f'nome: {self.nome}')
    print(f"telefone: {self.telefone}")
    print("="*30)

lista_cliente = []

print("==SOLICITANDO DADOS==")
for i in range(3):
    dados = Cliente(
        nome = input("digite seu nome: "),
        telefone = input("digite o tell para contato: "),
        email = input("digite seu email: ")
    )
    lista_cliente.append(dados)
print("==EXIBINDO DADOS==")
for cliente in lista_cliente:
    cliente.mostrar_dados()
    
print("==EXIBINDO EMAIL MARKETING==")
for cliente in lista_cliente:
    cliente.email_marketing()
    
print("==EXIBINDO WHATSAPP MARKETING==")
for cliente in lista_cliente:
    cliente.whatsapp_marketing()
    

