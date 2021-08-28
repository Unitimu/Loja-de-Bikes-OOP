from datetime import datetime, timedelta
import math


class Cliente(object):
    def verificarBikes(self, loja):
        print(loja.estoqueBikes)

    def verificarTempo(self, nBikes, stempo):
        try:
            if stempo not in ["horas", "dias", "semanas"]:
                raise Exception

            print(f"O aluguel de {nBikes} bicicletas será cobrado em {stempo}.")

        except:
            print(
                f'O sistema não reconhece o termo "{stempo}", por favor insira um formato de tempo desejado, como: "horas","dias" ou "semanas" '
            )

        return -1

    def alugarBikes(self, loja, bikes_a_alugar, stempo):

        try:
            if bikes_a_alugar == 0:
                raise ValueError
            if bikes_a_alugar > loja.estoqueBikes:
                raise SystemError(
                    "A loja não tem essa quantidade de bibicletas disponível no momento"
                )

            self.verificarTempo(bikes_a_alugar, stempo)
            formatoTempo = stempo
            loja.estoqueBikes -= bikes_a_alugar

            return formatoTempo, bikes_a_alugar

        except SystemError:
            print(
                f"A loja desejada possui {loja.estoqueBikes} bicletas no momento, não suportando um aluguel de {bikes_a_alugar}"
            )
            self.alugarBikes(loja)

        except ValueError:
            print("Por favor, insira um dígito válido")
            self.alugarBikes(loja)


# Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos (de qualquer tipo) com 30% de desconto no valor total.
class Loja(object):
    def __init__(self, estoqueBikes):
        self.estoqueBikes = estoqueBikes
        self.caixa = 0
        self.precoHora = 10
        self.precoDia = 180
        self.precoSemana = 900

    def mostraEstoque(self):
        """fazer um print do estoque de bikes"""

        if self.estoqueBikes > 1:
            print(f"\nEstoque de Bicicletas - {self.estoqueBikes} bikes.")

        elif self.estoqueBikes == 1:
            print(f"\nEstoque de Bicicletas - {self.estoqueBikes} bike.")

        else:
            print(f"\nEstoque de Bicicletas - Vazio no momento.")

    def valorTempoAluguelBikes(self, numeroBikes, stempo, tempoUsado):
        """Verifica o tempo que o cliente usufruiu das bikes e realiza a cobrança,
        tendo como parâmetros: Numero de Bikes(int), formato de cobrança(str) e o Tempo gasto(timedelta)
        """

        try:

            if stempo == "horas":
                tempoAdequado = math.ceil(tempoUsado.total_seconds() / 3600)
                valorConta = numeroBikes * (tempoAdequado * self.precoHora)
                print(
                    f"Pedido recebido - {numeroBikes} bicicletas durante {tempoAdequado} horas, total de R$ {valorConta} reais, pedido confirmado \nTotal bikes disponíveis no estoque: {self.estoqueBikes}."
                )
            if stempo == "dias":
                tempoAdequado = math.ceil(tempoUsado.total_seconds() / 3600 * 24)
                valorConta = numeroBikes * (tempoAdequado * self.precoDia)
                print(
                    f"Pedido recebido - {numeroBikes} bicicletas durante {tempoAdequado} horas, total de R$ {valorConta} reais, pedido confirmado \nTotal bikes disponíveis no estoque: {self.estoqueBikes}."
                )
            if stempo == "semanas":
                tempoAdequado = math.ceil(tempoUsado.total_seconds() / 3600 * 24 * 7)
                valorConta = numeroBikes * (tempoAdequado * self.precoSemana)
                print(
                    f"Pedido recebido - {numeroBikes} bicicletas durante {tempoAdequado} horas, total de R$ {valorConta} reais, pedido confirmado \nTotal bikes disponíveis no estoque: {self.estoqueBikes}."
                )

        except:
            print("Erro 404")


eu = Cliente()
lojinha = Loja(15)

stempo, nBikes = eu.alugarBikes(lojinha, 5, "horas")


n = timedelta(days=5, hours=3, weeks=2)
lojinha.valorTempoAluguelBikes(nBikes, stempo, n)
