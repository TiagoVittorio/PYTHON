"""CURSO DE PYTHON
@author: Tiago Condez   19/09/2025 
"""
# INPUT DE DADOS 
nome=input("Qual o seu nome?: ")
idade=int(input("Qual a sua idade? "))
curso=float(input ("Digite o valor do curso: "))
# PROCESSAMENTO DE DADOS
if(idade < 10 or idade > 70):
    print("ERRO!!!!!!!!!!!!! Não dispõe da idade para frequentar o curso.\n")
else:
    #OUTPUT DE DADOS
    print("Bem-Vindo ao Python", nome)
    print ("A Mentalidade do curso é de ", curso)

#FINALIZAÇÃO DO PROGRAMA
print("\n \n Prima ENTER para terminar...")
pausa=input()