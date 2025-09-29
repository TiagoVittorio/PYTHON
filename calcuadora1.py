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
operacao=input("Insira a operação (A or a , S or s , M or M , S or S, p or P): ")

# PROCESSAMENTO DE DADOS
match operacao:
    case "A or a":
        resultado = num1 + num2
    case "S or s":
        resultado = num1 - num2
    case "M or m":
        resultado = num1 * num2
    case "D or d":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero"
    case "p or P":
        resultado = math.pow(num1, num2)
    case _:
        resultado = "Erro: Operação inválida"
# OUTPUT DE DADOS
print(f"Resultado: {resultado}")
# Finalização do programa
print("\n \n Prima ENTER para terminar...")
pausa=input()
