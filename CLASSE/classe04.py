from dataclasses import dataclass 
import os 
os.system("cls")


@dataclass
class Cliente:
    nome :str
    idade : int
    altura : float
    peso = int
lista_cliente = []
print("==SOLICITANDO DADOS DE UM CLIENTE==")
for i in range(2):
    dados_do_cliente = Cliente(
        nome= input("\ndigite o nome do cliente: "),
        
        idade=int(input("digite a idade do cliente: ")),
        altura = float(input("digite a altura do cliente: ")),
        peso = int(input("digite seu peso: "))
        
    )
    lista_cliente.append(dados_do_cliente)
print("==EXIBINDO DADOS==")
for cliente in lista_cliente:
    print(f"nome: {cliente.nome}")
    print(f"idade: {cliente.idade}")
    print(f"altura: {cliente.altura}")
    print(f"peso: {cliente.peso}")
    print("="*15)
