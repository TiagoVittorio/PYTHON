"""
Abastração de um funcionario E aumentar o salario de um dos funcionarios
@tiago condez 2/2/2026
"""

# Função
def hifenes():
    print("-" * 52)

#Abstração da classe 
class Funcionario:
    #Construtor 
    def __init__(self,nome,nif,salario):
        #Atributos
        self.nome = nome
        self.nif = nif
        self.salario = salario
    #Método de instância
    def exibir_dados(self):
        print(f"Nome: {self.nome}\n")
        print(f"NIF: {self.nif}\n")
        print(f"Salário: {self.salario}\n")
#Programa principal
hifenes()
print("Funcinários") 
print("@ 2026 por Tiago Condez")
#Instanciando o 1º objeto funcionario1
funcionario1 = Funcionario("Joaquim", "123456789", 1000.00)
#Instanciando o 2º objeto funcionario2
funcionario2 = Funcionario("Maria", "987654321", 1500.00 )
#Instanciando o 3º objeto funcionario3
funcionario3 = Funcionario("Ana", "456789123", 2000.00)
#Visualização dos objetos   
funcionario1.exibir_dados()
hifenes()
funcionario2.exibir_dados()
hifenes()
funcionario3.exibir_dados()
hifenes()
#Aumentar o salário do funcionario2 em 10%
funcionario2.salario *= 1.10
print("Após o aumento de 10% no salário de Maria:")
funcionario2.exibir_dados()
hifenes()
#Finalização
print("\n Prima ENTER para terminar...")
pausa = input()