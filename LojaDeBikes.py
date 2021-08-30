from datetime import datetime, timedelta
import math


class Cliente(object):
    def verificarTempo(self, nBikes, stempo):  # testado
        try:
            if stempo not in ["horas", "dias", "semanas"]:
                raise Exception

            print(f"O aluguel de {nBikes} bicicletas será cobrado em {stempo}.")
            return -1

        except:
            print(
                f'O sistema não reconhece o termo "{stempo}", por favor insira um formato de tempo desejado, como: "horas","dias" ou "semanas" '
            )
            return 0

    def alugarBikes(self, loja, bikes_a_alugar, stempo):  # testado
        familia = False

        try:
            if bikes_a_alugar == 0:
                raise ValueError
            if type(bikes_a_alugar) != int:
                raise ValueError
            if bikes_a_alugar > loja.estoqueBikes:
                raise SystemError(
                    "A loja não tem essa quantidade de bibicletas disponível no momento"
                )

            self.verificarTempo(bikes_a_alugar, stempo)
            formatoTempo = stempo
            loja.estoqueBikes -= bikes_a_alugar

            if 5 >= bikes_a_alugar >= 3:
                familia = True
                print(
                    f"Como você fez um aluguel de {bikes_a_alugar} bicicletas, você acabou de ganhar um desconto de 30% por conta do Pacote Família!"
                )

            return (
                familia,
                bikes_a_alugar,
                formatoTempo,
            )

        except SystemError:
            print(
                f"A loja desejada possui {loja.estoqueBikes} bicletas no momento, não suportando um aluguel de {bikes_a_alugar}"
            )
            return -1

        except ValueError:
            print("Por favor, insira um dígito válido")
            return 0


# Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos (de qualquer tipo) com 30% de desconto no valor total.
class Loja(object):
    def __init__(self, estoqueBikes):
        self.estoqueBikes = estoqueBikes
        self.caixa = 0
        self.precoHora = 10
        self.precoDia = 180
        self.precoSemana = 900

    def mostraEstoque(self):  # testado
        """fazer um print do estoque de bikes"""
        try:
            if not isinstance(self.estoqueBikes, int):
                raise ValueError

            if self.estoqueBikes > 1:
                print(f"\nEstoque de Bicicletas - {self.estoqueBikes} bikes.")

            elif self.estoqueBikes == 1:
                print(f"\nEstoque de Bicicletas - {self.estoqueBikes} bike.")

            else:
                print(f"\nEstoque de Bicicletas - Vazio no momento.")

            return -1
        except ValueError:
            print("Você imputou um valor não coerente, ajustar")
            return 0

    def valorTempoAluguelBikes(
        self, numeroBikes, stempo, tempoUsado, promoFamilia=False
    ):
        """Verifica o tempo que o cliente usufruiu das bikes e realiza a cobrança,
        tendo como parâmetros: Numero de Bikes(int), formato de cobrança(str) e o Tempo gasto(timedelta)
        """

        descontoFamilia = 1

        try:
            if not isinstance(promoFamilia, bool):
                raise TypeError

            if promoFamilia:
                descontoFamilia = 0.7

            tempoHoras = tempoUsado.total_seconds() / 3600

            if stempo not in ["horas", "dias", "semanas"]:
                raise AttributeError

            if stempo == "horas":

                tempoAdequado = math.ceil(tempoHoras)
                valorConta = (
                    numeroBikes * (tempoAdequado * self.precoHora) * descontoFamilia
                )
                print(
                    f"Pedido recebido: {numeroBikes} bicicletas durante {tempoAdequado} horas."
                )
                print(
                    f"Preço Hora: R${self.precoHora * descontoFamilia:.2f}\nTotal: R${valorConta:.2f}"
                )

            if stempo == "dias":
                tempoAdequado = math.ceil(tempoHoras / 24)
                valorConta = (
                    numeroBikes * (tempoAdequado * self.precoDia) * descontoFamilia
                )
                print(
                    f"Pedido recebido: {numeroBikes} bicicletas durante {tempoAdequado} dias ({tempoHoras} horas)."
                )
                print(
                    f"Preço Dia: R${self.precoDia * descontoFamilia:.2f}\nTotal: R${valorConta:.2f}"
                )

            if stempo == "semanas":
                tempoAdequado = math.ceil(tempoHoras / (24 * 7))
                valorConta = (
                    numeroBikes * (tempoAdequado * self.precoSemana) * descontoFamilia
                )
                print(
                    f"Pedido recebido: {numeroBikes} bicicletas durante {tempoAdequado} semanas ({tempoHoras} horas)."
                )
                print(
                    f"Preço Semana: R${self.precoSemana * descontoFamilia:.2f}\nTotal: R${valorConta:.2f}"
                )
            self.estoqueBikes += numeroBikes
            return -1

        except TypeError:
            print("Argumento promofamilia não booleano, corrigir ")
            return -2

        except AttributeError:
            print("Você não inseriu dias/semanas/horas, corrigir")
            return -3

        except:
            print("Erro 404")
            return 0


eu = Cliente()
lojinha = Loja(15)
promoFamilia, nBikes, stempo = eu.alugarBikes(lojinha, 5, "dias")
tempoAluguel = timedelta(days=5, hours=3, weeks=2)
lojinha.valorTempoAluguelBikes(nBikes, stempo, tempoAluguel, promoFamilia)
