from aplicacao import Aplicacao


class Cdi(Aplicacao):
    def __init__(self, nome, capital, tempo, taxaJuros, montante, juros, ir):
        self.ir = ir
        super().__init__(nome, capital, tempo, taxaJuros, montante, juros)

    def entrada(self):
        self.nome = input("Digite seu nome: ")
        self.capital = float(input("Digite a quantia em reais a ser investida: "))
        self.tempo = int(input("Digite a quantidade de meses que seu dinheiro ficará investido"))
        self.taxaJuros = (float(input("Digite a taxa de juros anual: "))/100)/12

    def calculaJurosCdi(self):
        self.juros = self.capital * self.taxaJuros * self.tempo
        self.montante = self.capital + self.juros
        if self.tempo <= 6:
            self.ir = self.juros*0.255

        elif self.tempo > 6 and self.tempo <= 12:
            self.ir = self.juros*0.2

        elif self.tempo > 12 and self.tempo <= 24:
            self.ir = self.juros*0.175

        else:
            self.ir = self.juros*0.15
