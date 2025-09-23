""" CALCULO DE PERIMETRO E AREA DE UM CIRCULO
@author: Tiago Condez   22/09/2025 
"""
# INPUT DE DADOS
nome=(input("Qual o nome do Programador? : "))

raio=float(input("Qual o valor do raio do circulo? : "))
# PROCESSAMENTO DE DADOS
PI=3.14
perimetro=2*PI*raio
area=PI*raio*raio
# OUTPUT DE DADOS
print("O perimetro do circulo é: ", perimetro)
print("A area do circulo é: ", area)

# Finalização do programa
print("\n \n Prima ENTER para terminar...")
pausa=input()

