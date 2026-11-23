from dataclasses import dataclass 
import os 
os.system("cls")


@dataclass
class Cliente:
    nome :str
    idade : int

#SOLICITANDO DADOS DE UM CLIENTE 
cliente = Cliente("marta", 30)

#SOLICITANDO DADOS DE OUTRO CLIENTE 
cliente2 = Cliente("josé", 40)


print(f"nome: {cliente.nome}")
print(f"idade: {cliente.idade}")


print(f"nome: {cliente2.nome}")
print(f"idade: {cliente2.idade}")