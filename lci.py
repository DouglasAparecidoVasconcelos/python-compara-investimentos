from aplicacao import Aplicacao


class Lci(Aplicacao):
    def __init__(self, capital, tempo, taxaJuros, montante, juros):
        super().__init__(capital, tempo, taxaJuros, montante, juros)

    def entrada(self):
        self.capital = float(input("Digite a quantia em reais a ser investida: "))
        self.tempo = int(input("Digite a quantidade de meses que seu dinheiro ficará investido: "))

        while self.tempo < 12:
            self.tempo = input("Este tipo de aplicação só permite um tempo maior ou igual a 12 meses\nDigite novamente o tempo que deseja aplicar seu dinheiro: ")

        self.taxaJuros = (float(input("Digite a taxa de juros anual: "))/100)/12
        # self.taxaJuros = 0.1414 14,14

    def calculaJurosLci(self):
        self.juros = self.capital * self.taxaJuros * self.tempo
        self.montante = self.capital + self.juros

    def saida(self):
        print("Se investido seu dinheiro no LCI, seus resultados financeiros serão:")
        print("Dinheiro investido: ", self.capital)
        print("Seu dinheiro rendeu: ", self.juros)
        print("Saldo total após aplicação: ", self.montante)
