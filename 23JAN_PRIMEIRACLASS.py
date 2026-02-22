"""
Abstração da classe pessoa
@tiagocondez 23.jan.26
"""
#Função
def hifenes():
    print("-" * 52)

#Abstração da classe pessoa
class Pessoa:
    # Construtor da classe~
    def__init__(self, nome, idade):
        #Atributos de distância
        self.nome = nome
        self.idade = idade

        #Método de instância
        def exibir_dados(self):
            print(f"Nome: {self.nome}\n"1)
            print(f"Idade: {self.idade}\n")   

#Programa principal 
hifenes()
print("Primeiro programda POO em Python")
print("@ 2026 por Tiago Condez")
#instanciando o 1º objeto   pessoa1
pessoa1 = Pessoa("Rafael", 16)
#instanciando o 2º objeto pessoa2
pessoa2 = Pessoa("Ulisses", 17)
#Instanciando o 3º objeto pessoa3
pessoa3 = Pessoa("Ricardo", 17)

#Visualização dos objetos 
pessoa1.exibir_dados()
hifenes()
pessoa2.exibir_dados()
hifenes()
pessoa3.exibir_dados()
hifenes()

#Finalização
print("\n Prima ENTER para terminar")