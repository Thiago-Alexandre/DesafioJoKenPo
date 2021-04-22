class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.vitorias = 0
        self.cartas_mao = []

    def __str__(self):
        return self.nome

    def iniciar_mao(self, baralho):
        self.cartas_mao.clear()
        for i in range(3):
            self.cartas_mao.append(baralho.disponibilizar_nova_carta())

    def ver_mao(self):
        print(f"Cartas na mão do Jogador {self.nome}:")
        for posicao in range(len(self.cartas_mao)):
            print(f"\t{posicao + 1}\t{self.cartas_mao[posicao].nome_tipo}")

    def selecionar_carta(self, posicao_carta):
        carta_selecionada = self.cartas_mao[posicao_carta - 1]
        self.cartas_mao.pop(posicao_carta - 1)
        return carta_selecionada
