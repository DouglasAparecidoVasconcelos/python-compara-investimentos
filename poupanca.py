from aplicacao import Aplicacao


class Poupanca(Aplicacao):
    def __init__(self,nome, capital, tempo):
        super().__init__(nome,capital,tempo)
