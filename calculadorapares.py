""" Calculadora de Números pares
@author: Tiago Condez   29/09/2025 
"""

#INPUT DE DADOS
print("PROCESSAMENTO DE NUMEROS PARES DE 1 ATÉ 100\n")
print("Programador : Tiago Condez")

#Processamneto
print("Lista de Números pares")
contador=0  # Contador = Conta as repetições dos números pares
soma=0 # Acumulador = Soma os sucessivos números pares
for i in range(1,101): 
    if(i % 2 == 0): # Verifica se o número é par
        print( f"{i} " ,end="") # Imprime o número par
        contador=contador+1
        soma = soma + i
print(f"\n\n Foram exibidos {contador} números.\nSomas = {soma}")

#FINALIZAÇÃO
print("\n \n Prima ENTER para terminar...")
pausa=input()

       