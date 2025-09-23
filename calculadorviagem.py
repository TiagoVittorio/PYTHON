""" CALCULADORA DO CUSTO DE UMA VIAGEM
@author: Tiago Condez  22/09/2025 
"""

# INPUT DE DADOS
nome=input("Qual o nome do Programador? : ")
consumo=float(input("Qual o consumo médio em km/l00? : "))
distancia=float(input("Qual a distância em km da viagem? : "))
preco=float(input("Qual o preço do combustível em € ? : "))

# PROCESSAMENTO DE DADOS
litro_gastos= (consumo* distancia)/100
custo  = litro_gastos* preco  

# OUTPUT DE DADOS
print("O custo da viagem é: ",custo, "euros")
print("Litros de combustível gastos: ",litro_gastos, "litros" )
# Finalização do programa
print("\n \n Prima ENTER para terminar...")
pausa=input()
