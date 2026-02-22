"""
Abastração de carro para aluguel
@tiago condez 2/2/2026
"""
# Função
def hifenes():
    print("-" * 52)
#Abstração da classe
class Carro:
    #Construtor 
    def __init__(self, marca, modelo, preço ,valor_final, dias_aluguel):
        #Atributos
        self.marca = marca
        self.modelo = modelo
        self.preço = preço
        self.dias_aluguel = dias_aluguel
        self.valor_final = valor_final
    #Método para calcular o valor final do aluguel
    def calcular_valor_final(self, dias):
        self.dias_aluguel = dias
        self.valor_final = self.preço * dias
    #Método de instância
    def exibir_dados(self):
        print(f"Marca: {self.marca}\n")
        print(f"Modelo: {self.modelo}\n")
        print(f"Preço por dia: {self.preço}\n")
        print(f"Dias de aluguel: {self.dias_aluguel}\n")
        print(f"Valor final do aluguel: {self.valor_final}\n")
#Programa principal
hifenes()
print("Aluguel de Carros")
print("@ 2026 por Tiago Condez")
#Instanciar o 1º objeto carro1
carro1 = Carro("Toyota", "Corolla", 50.00, 4)
#Instanciar o 2º objeto carro2    
carro2 = Carro("Honda", "Civic", 60.00, 2)
#Instanciar o 3º objeto carro3
carro3 = Carro("Ford", "Focus", 55.00, 5)
#Visualização dos objetos
carro1.exibir_dados()
hifenes()
carro2.exibir_dados()
hifenes()
carro3.exibir_dados()
hifenes()
#Finalização
print("\n Prima ENTER para terminar...")
pausa = input()
     