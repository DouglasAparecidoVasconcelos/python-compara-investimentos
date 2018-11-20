from poupanca import Poupanca
from cdi import Cdi
from lci import Lci

nome = ""
montante = 0.0
juros = 0.0
ir = 0.0
opcao = 100


while opcao != 0:
    try:
        opcao = int(input("Digite:\n1-para simulação\n2-para investimento\n0-para SAIR\n"))
        if opcao == 1:
            print("SIMULAÇÃO")

            nome = input("Digite seu nome:\n")
            capital = float(input("Digite a quantia em reais a ser investida: \n"))
            tempo = int(input("Digite a quantidade de meses que seu dinheiro ficará investido: \n"))

            poupanca = Poupanca(nome, capital, tempo, 0.0827/12, montante, juros)
            poupanca.calculaJurosPoupanca()
            poupanca.saida()

            cdi = Cdi(nome, capital, tempo, 0.1372/12, montante, juros, ir)
            cdi.calculaJurosCdi()
            cdi.saida()

            lci = Lci(nome, capital, tempo, 0.1414/12, montante, juros)
            lci.calculaJurosLci()
            lci.saida()

            if poupanca.montante > cdi.montante and poupanca.montante > lci.montante:
                print("\nO investimento na POUPANÇA é o mais rentável !!!")
            elif cdi.montante > poupanca.montante and cdi.montante > lci.montante:
                print("\nO investimento na CDI é o mais rentável !!!")
            else:
                print("\nO investimento na LCI é o mais rentável !!!")

        if opcao == 2:
            opcao2 = int(input("Digite:\n1-para POUPANÇA\n2-para CDI\n3-para LCI\n0-para voltar ao menu anterior:\n"))

            while opcao2 != 0:

                if opcao2 == 1:
                    poupanca = Poupanca(0, 0, 0, 0, 0, 0)
                    poupanca.entrada()
                    Poupanca.calculaJurosPoupanca()
                    poupanca.saida()

                elif opcao2 == 2:
                    cdi = Cdi(0, 0, 0, 0, 0, 0, 0)
                    cdi.entrada()
                    cdi.calculaJurosCdi()
                    cdi.saida()

                elif opcao2 == 3:
                    lci = Lci(0, 0, 0, 0, 0, 0)
                    lci.entrada()
                    lci.calculaJurosLci()
                    lci.saida()
    except ValueError:
        print("O valor inserido está incorreto, tente novamente\n")
