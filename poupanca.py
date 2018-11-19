from aplicacao import Aplicacao


class Poupanca(Aplicacao):
    def __init__(self, nome, capital, tempo, taxaJuros, montante, juros):
        super().__init__(nome, capital, tempo, taxaJuros, montante, juros)

    def entrada(self):
        self.nome = input("Digite seu nome: ")
        self.capital = float(input("Digite a quantia em reais a ser investida: "))
        self.tempo = int(input("Digite a quantidade de meses que seu dinheiro ficará investido"))
        self.taxaJuros = (float(input("Digite a taxa de juros anual: "))/100)/12
        # self.taxaJuros = 0.0827

    def calculaJurosPoupanca(self):
        self.juros = self.capital * self.taxaJuros * self.tempo
        self.montante = self.capital + self.juros

    def saida(self):
        print("Se investido seu dinheiro na POUPANÇA, seus resultados financeiros serão:")
        print("Dinheiro investido: ", self.capital)
        print("Seu dinheiro rendeu: ", self.juros)
        print("Saldo total após aplicação: ", self.montante)
