from poupanca import Poupanca
from cdi import Cdi
from lci import Lci

nome = ""
capital = 0.0
tempo = 0
taxaJuros = 0.0
montante = 0.0
juros = 0.0

pessoa1 = Poupanca(nome, capital, tempo, taxaJuros, montante, juros)
pessoa2 = Cdi(0,0,0,0,0,0,0)

pessoa1.entrada()
pessoa1.calculaJurosPoupanca()
pessoa1.saida()

pessoa2.entrada()
pessoa2.calculaJurosCdi()
pessoa2.saida()

