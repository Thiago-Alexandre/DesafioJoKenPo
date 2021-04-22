import random


class Baralho:

    def __init__(self):
        self.cartas = []

    def embaralhar_baralho(self):
        for i in range(10):
            self.cartas.append(Pedra())
        for i in range(10):
            self.cartas.append(Tesoura())
        for i in range(10):
            self.cartas.append(Papel())
        random.shuffle(self.cartas)

    def disponibilizar_nova_carta(self):
        if self.cartas:
            carta = self.cartas.pop(0)
            return carta
        return None


class Tipo:
    """
    Classe base para os tipos de cartas e suas eficacias.
    """

    def __init__(self, nome: str, tipo: str):
        self.nome_tipo = nome
        self.tipo_eficaz = tipo

    def verificar_eficacia(self, tipo) -> bool:
        if self.tipo_eficaz == tipo.nome_tipo:
            return True
        return False


class Pedra(Tipo):

    def __init__(self):
        super().__init__("Pedra", "Tesoura")

    def __str__(self):
        return self.nome_tipo


class Tesoura(Tipo):

    def __init__(self):
        super().__init__("Tesoura", "Papel")

    def __str__(self):
        return self.nome_tipo


class Papel(Tipo):

    def __init__(self):
        super().__init__("Papel", "Pedra")

    def __str__(self):
        return self.nome_tipo
