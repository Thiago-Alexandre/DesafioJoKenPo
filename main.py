from Jogo import Jogo


class Main:

    def __init__(self):
        while self.solicitar_resposta("Deseja iniciar um jogo com novos jogadores?\n\tS - Sim\n\tN - Não\n"):
            print("-" * 100)
            print("Iniciando Jogo...\n")
            jogador1 = input("Digite o nome do Jogador 1:\n")
            jogador2 = input("Digite o nome do Jogador 2:\n")
            self.jogo = Jogo(jogador1, jogador2)
            while self.solicitar_resposta("Deseja iniciar uma nova rodada?\n\tS - Sim\n\tN - Não\n"):
                self.jogo.iniciar_jogo()
        print("Finalizando sistema...")

    def solicitar_resposta(self, mensagem):
        print("-" * 100)
        novo = input(mensagem)
        if novo.lower() != "s":
            return False
        return True


if __name__ == '__main__':
    Main()
