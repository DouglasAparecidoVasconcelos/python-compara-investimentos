class Aplicacao:
    def __init__(self, nome, capital, tempo, taxaJuros, montante,juros):
        self.nome = nome
        self.capital = capital
        self.tempo = tempo
        self.taxaJuros = taxaJuros
        self.montante = montante
        self.juros = juros

    def entrada(self):
        self.nome = input("Digite seu nome: ")
        self.capital = float(input("Digite a quantia em reais a ser investida: "))
        self.tempo = int(input("Digite a quantidade de meses que seu dinheiro ficará investido"))
        self.taxaJuros = float(input("Digite a taxa de juros anual: "))

    def saida(self):
        print()


