class Aplicacao:
    def __init__(self, nome, capital, tempo):
        self.nome = nome
        self.capital = capital
        self.tempo = tempo

    def entrada(self):
        self.nome = input("Digite seu nome: ")
        self.capital = float(input("Digite a quantia em reais a ser investida: "))
        self.tempo = int(input("Digite a quantidade de meses que seu dinehiro ficará investido"))

