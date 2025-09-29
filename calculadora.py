""" Calculadora simples
@author: Tiago Condez   29/09/2025 
"""
#Cabeçalho do programa
import math

# INPUT DE DADOS

print("Calculadora Simples")
print("Programador : Tiago Condez")
num1=float(input("Insira o primeiro número: "))
num2=float(input("Insira o segundo número: "))

# PROCESSAMENTO DE DADOS
print("MENU")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")
opcao=int(input("Escolha a operação (1-5): "))
if opcao == 1:
    resultado = num1 + num2
    operacao = "Adição"
elif opcao == 2:
    resultado = num1 - num2
    operacao = "Subtração"
elif opcao == 3:
    resultado = num1 * num2
    operacao = "Multiplicação"
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        operacao = "Divisão"
    else:
        resultado = "Erro: Divisão por zero"
        operacao = "Divisão"
elif opcao == 5:
    resultado = math.pow(num1, num2)
    operacao = "Potenciação"
else:
    resultado = "Erro: Opção inválida"
    operacao = "N/A"
# OUTPUT DE DADOS
print(f"Operação: {operacao}")
print(f"Resultado: {resultado}")
# Finalização do programa
print("\n \n Prima ENTER para terminar...")
pausa=input()