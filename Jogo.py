from Jogador import Jogador
from Baralho import Baralho


class Jogo:

    def __init__(self, nome_jogador1, nome_jogador2):
        self.jogador1 = Jogador(nome_jogador1)
        self.jogador2 = Jogador(nome_jogador2)

    def iniciar_jogo(self):
        print("-" * 100)
        self.jogador1.vitorias = self.jogador2.vitorias = 0
        print("Carregando baralho...")
        baralho = Baralho()
        baralho.embaralhar_baralho()
        for c in range(len(baralho.cartas)):
            print(f"\t{c} - {baralho.cartas[c]}")
        for r in range(5):
            self.iniciar_rodada(baralho)
        print(f"Vitórias do Jogador {self.jogador1.nome}: {self.jogador1.vitorias}!")
        print(f"Vitórias do Jogador {self.jogador2.nome}: {self.jogador2.vitorias}!")

    def iniciar_rodada(self, baralho):
        print("-" * 100)
        for j in range(len(baralho.cartas)):
            print(f"\t{j} - {baralho.cartas[j]}")
        print(f"Carregando cartas do {self.jogador1}")
        self.jogador1.iniciar_mao(baralho)
        print(f"Carregando cartas do {self.jogador2}")
        self.jogador2.iniciar_mao(baralho)
        empate = 0
        for i in range(3):
            print(f"Round {i + 1}")
            if self.iniciar_round():
                break
            empate += 1
            if empate == 3:
                print("Ninguém ganhou!")
                break

    def iniciar_round(self):
        carta_selecionada_jogador1 = self.solicitar_carta(self.jogador1)
        carta_selecionada_jogador2 = self.solicitar_carta(self.jogador2)
        vencedor_rodada = self.verificar_vencedor(carta_selecionada_jogador1, carta_selecionada_jogador2)
        if vencedor_rodada is not None:
            vencedor_rodada.vitorias += 1
            print(f"Vencedor {vencedor_rodada}!")
            return True
        else:
            print("Empate!")
            return False

    def solicitar_carta(self, jogador):
        print("-" * 100)
        try:
            jogador.ver_mao()
            if len(jogador.cartas_mao) > 1:
                carta_selecionada_jogador = jogador.selecionar_carta(
                    int(input(f"Jogador {jogador}, selecione qual carta deseja jogar:\n")))
            else:
                carta_selecionada_jogador = jogador.cartas_mao[0]
            return carta_selecionada_jogador
        except Exception as error:
            print(error)
            print("Carta não encontrada!")
            self.solicitar_carta(jogador)

    def verificar_vencedor(self, carta_selecionada_jogador1, carta_selecionada_jogador2):
        if carta_selecionada_jogador1.verificar_eficacia(carta_selecionada_jogador2):
            return self.jogador1
        elif carta_selecionada_jogador2.verificar_eficacia(carta_selecionada_jogador1):
            return self.jogador2
        else:
            return None
