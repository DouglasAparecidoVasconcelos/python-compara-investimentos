from poupanca import Poupanca
from cdi import Cdi
from lci import Lci

nome = ""
taxaJuros = 0.0
montante = 0.0
juros = 0.0
ir = 0.0
opcao = 100

while opcao != 0:
    opcao = int(input("Digite:\n1-para simulação\n2-para investimento\n3-para SAIR\n"))
    if opcao == 1:
        print("SIMULAÇÃO")
        
        nome = input("Digite seu nome: ")
        capital = float(input("Digite a quantia em reais a ser investida: \n"))
        tempo = int(input("Digite a quantidade de meses que seu dinheiro ficará investido: "))


        poupanca = Poupanca(nome, capital, tempo, 8.27, montante, juros)
        cdi = Cdi(nome, capital, tempo, taxaJuros, montante, juros, ir)
        lci = Lci(nome, capital, tempo, taxaJuros, montante, juros)


pessoa2 = Cdi(0, 0, 0, 0, 0, 0, 0)

pessoa1.entrada()
pessoa1.calculaJurosPoupanca()
pessoa1.saida()

pessoa2.entrada()
pessoa2.calculaJurosCdi()
pessoa2.saida()

