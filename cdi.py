from aplicacao import Aplicacao


class Cdi(Aplicacao):
    def __init__(self, nome, capital, tempo):
        super().__init__(nome, capital, tempo)

    def entrada(self):
        self.nome = input("Digite seu nome: ")
        self.capital = float(input("Digite a quantia em reais a ser investida: "))
        self.tempo = int(input("Digite a quantidade de meses que seu dinheiro ficará investido"))
        self.taxaJuros = (float(input("Digite a taxa de juros anual: "))/100)/12

