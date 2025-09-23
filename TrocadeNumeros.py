""" TROCA DE NUMEROS REAIS ENTRE DUAS VARIAVEIS
@author: Tiago Condez   22/09/2025 
"""

#Input de dados 

A = float(input("Variavel A?"))
B = float(input("Variavel B?"))

# Processamento de dados

auxilar = A
A = B
B = auxilar 

#OUTPUT DE DADOS

print("Valor de A = ", A )
print ("Valor de B = ", B )

#FINALIZAÇÃO

print("\n \n Prima ENTER para terminar...")
pausa=input()