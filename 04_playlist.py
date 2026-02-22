# Declaração de Função
def hifenes():
    print("-" * 52)


# Programa principal
hifenes()
print("PLAYLIST DE UM ESTILO MUSICAL")
print("@ 2026 por Tiago Condez")
hifenes()


# Declaração de classe 
class Playlist:
    # Construtor
    def __init__(self, estilo):
        self.estilo = estilo
        self.musicas = []

    # Adicionar música
    def add_musica(self, musica):
        self.musicas.append(musica)
        print("Música adicionada com sucesso:", musica)

    # Remover música
    def remove_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            print("Música removida com sucesso:", musica)
        else:
            print("Música não encontrada na playlist.")

    # Mostrar playlist
    def show_playlist(self):
        print(f"\nPlaylist de {self.estilo}:")
        if not self.musicas:
            print("Playlist vazia.")
        else:
            for musica in self.musicas:
                print(f"- {musica}")


# Declaração da classe 
class Utilizador:
    def __init__(self, nome):
        self.nome = nome
        self.playlist = None

    # Criar playlist
    def criar_playlist(self, estilo):
        self.playlist = Playlist(estilo)
        print(f"Playlist de {estilo} criada com sucesso!")


# Programa principal
nome = input("Nome do utilizador: ")
user = Utilizador(nome)

while True:
    hifenes()
    print("MENU")
    print("1 - Criar playlist")
    print("2 - Adicionar música")
    print("3 - Remover música")
    print("4 - Ver playlist")
    print("0 - Sair")
    hifenes()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        estilo = input("Introduza o estilo musical: ")
        user.criar_playlist(estilo)

    elif opcao == "2":
        if user.playlist:             
            musica = input("Nome da música: ")
            user.playlist.add_musica(musica)
        else:
            print("Crie uma playlist primeiro!")

    elif opcao == "3":
        if user.playlist:
            musica = input("Nome da música a remover: ")
            user.playlist.remove_musica(musica)
        else:
            print("Crie uma playlist primeiro!")

    elif opcao == "4":
        if user.playlist:
            user.playlist.show_playlist()
        else:
            print("Crie uma playlist primeiro!")

    elif opcao == "0":
        print("Programa terminado.")
        break

    else:
        print("Opção inválida!")


input("\nPrima ENTER para terminar...")
