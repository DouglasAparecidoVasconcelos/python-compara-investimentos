from aplicacao import Aplicacao


class Lci(Aplicacao):
    def __init__(self, nome, capital, tempo, taxaJuros, montante, juros):
        super().__init__(nome, capital, tempo, taxaJuros, montante, juros)

    def entrada(self):
        self.nome = input("\nDigite seu nome: ")
        self.capital = float(input("Digite a quantia em reais a ser investida:\n"))
        self.tempo = int(input("Digite a quantidade de meses que seu dinheiro ficará investido: "))

        while self.tempo < 12:
            self.tempo = int(input("Este tipo de aplicação só permite um tempo maior ou igual a 12 meses\nDigite novamente o tempo que deseja aplicar seu dinheiro: "))

        self.taxaJuros = (float(input("Digite a taxa de juros anual: "))/100)/12

    def calculaJurosLci(self):
        if self.tempo >= 12:
            self.juros = self.capital * self.taxaJuros * self.tempo
            self.montante = self.capital + self.juros
        else:
            self.montante = self.capital
            self.juros = 0.0
            print("\nNo periodo informado não há rendimento devido a liquidez.")

    def saida(self):
        print("\nCaro senhor ", self.nome)
        print("Se investido seu dinheiro no LCI, seus resultados financeiros serão:")
        print("Dinheiro investido: ", self.capital)
        print("Seu dinheiro rendeu: %.2f" % self.juros)
        print("Saldo total após aplicação: %.2f" % self.montante)
