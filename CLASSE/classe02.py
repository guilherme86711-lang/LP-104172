from dataclasses import dataclass 
import os 
os.system("cls")


@dataclass
class Cliente:
    nome :str
    idade : int
lista_cliente = []
#SOLICITANDO DADOS DE UM CLIENTE
lista_cliente.append(Cliente("marta", 30)) 
lista_cliente.append(Cliente("josé", 40)) 

for cliente in lista_cliente:
    print(f"nome: {cliente.nome}")
    print(f"nome: {cliente.idade}")
    print("="*15)
