"""
Clinica de obscidades - Cálculo do IMC  | E validar a idade para não ser menor que 0 e maior que 100 | e pedir para meter os numeros da altura e peso
@tiago condez 3/2/2026
"""
# Função
def hifenes():
    print("-" * 52)
#Abstração da classe
class Paciente:
    #Construtor 
    def __init__(self, nome, idade, peso, altura, imc):
        #Atributos
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.imc = imc
    #Método para calcular o IMC
    def calcular_imc(self):
        self.imc = self.peso / (self.altura ** 2)
    #Método de instância
    def exibir_dados(self):
        print(f"Nome: {self.nome}\n")
        print(f"Idade: {self.idade}\n")
        print(f"Peso: {self.peso} kg\n")
        print(f"Altura: {self.altura} m\n")
        print(f"IMC: {self.imc:.2f}\n")
#Programa principal
hifenes()
print("Clínica de Obesidades - Cálculo do IMC")
print("@ 2026 por Tiago Condez")
#Instanciar o 1º objeto paciente1
while True:
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    if 0 <= idade <= 100:
        break
    else:
        print("Idade inválida. Por favor, insira uma idade entre 0 e 100.")
peso = float(input("Digite o peso do paciente (kg): "))
altura = float(input("Digite a altura do paciente (m): "))
paciente1 = Paciente(nome, idade, peso, altura, 0)
paciente1.calcular_imc()
#Visualização do objeto
paciente1.exibir_dados()
hifenes()
#Finalização
print("\n Prima ENTER para terminar...")
pausa = input()
