from poupanca import Poupanca
from cdi import Cdi
from lci import Lci

pessoa1 = Poupanca(0,0,0,0,0,0)
pessoa2 = Cdi(0,0,0,0,0,0,0)

pessoa1.entrada()
pessoa1.calculaJurosPoupanca()
pessoa1.saida()

pessoa2.entrada()
pessoa2.calculaJurosCdi()
pessoa2.saida()

