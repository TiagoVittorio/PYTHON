""" Peso de uma pessoa noutro planeta
@author: Tiago Condez   29/09/2025 
"""

# INPUT DE DADOS
print("Peso de uma pessoa noutro planeta")
print("Programador : Tiago Condez")
peso=float(input("Insira o seu peso em kg: "))

# PROCESSAMENTO DE DADOS
print("Menu:")
print("1 - Mercúrio")
print("2 - Vénus")
print("3 - Marte")
print("4 - Júpiter")
print("5 - Saturno")
print("6 - Urano")
print("7- Lua")

planeta=int(input("Escolha o planeta (1-5): "))

# OUTPUT DE DADOS
match planeta:
    case 1:
        peso_planeta = peso * 0.38
        nome_planeta = "Mercúrio"
    case 2:
        peso_planeta = peso * 0.91
        nome_planeta = "Vénus"
    case 3:
        peso_planeta = peso * 0.38
        nome_planeta = "Marte"
    case 4:
        peso_planeta = peso * 2.34
        nome_planeta = "Júpiter"
    case 5:
        peso_planeta = peso * 1.06
        nome_planeta = "Saturno"
    case 6:
        peso_planeta = peso * 0.92
        nome_planeta = "Urano"
    case 7:
        peso_planeta = peso * 0.16
        nome_planeta = "Lua"
    case _:
          resultado = "Erro: Operação inválida"

print(f"Seu peso em {nome_planeta} é: {peso_planeta:.2f} kg")
# Finalização do programa
print("\n \n Prima ENTER para terminar...")
pausa=input()