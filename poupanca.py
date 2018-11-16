from aplicacao import Aplicacao


class Poupanca(Aplicacao):
    def __init__(self, nome, capital, tempo, montante, taxaJuros, juros):
        super().__init__(nome, capital, tempo,taxaJuros, montante, juros)

    def entrada(self):
        self.nome = input("Digite seu nome: ")
        self.capital = float(input("Digite a quantia em reais a ser investida: "))
        self.tempo = int(input("Digite a quantidade de meses que seu dinheiro ficará investido"))
        self.taxaJuros = (float(input("Digite a taxa de juros anual: "))/100)/12
        print(self.taxaJuros)

    def geraRentabilidadePoupanca(self):
        self.juros = self.capital * self.taxaJuros * self.tempo
        self.montante = self.capital + self.juros

    def saida(self):
        print("Montante após investimento: ", self.montante)
