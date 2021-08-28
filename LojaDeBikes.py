import datetime

class Cliente(object):
    def verificarBikes(self, loja):
        print(loja.estoqueBikes)

    def verificarTempo(self, stempo):
        try:
            if stempo not in ["horas", "dias", "semanas"]:
                raise Exception

        except:
            print(
                f'O sistema não reconhece o termo "{stempo}", por favor insira o formato do tempo desejado como: "horas","dias" ou "semanas" '
            )
        return -1

    def alugarBikes(self, loja):

        try:
            bikes_a_alugar = int(input("Quantas bicicletas você deseja alugar? "))

            if bikes_a_alugar == 0:
                raise ValueError
            if bikes_a_alugar > loja.estoqueBikes:
                raise SystemError(
                    "A loja não tem essa quantidade de bibicletas disponível no momento"
                )

            # Mostrar a tabela de preços pro usuário
            print(
                f"Os preços da loja são de :\nPreço/hora:R${loja.precoHora},\nPreço/dia:R${loja.precoDia},\nPreço/semanaR$:{loja.precoSemana}"
            )

            self.verificarTempo()
            agora = datetime.datetime.now()

            return agora, bikes_a_alugar

        except SystemError:
            print(
                f"A loja desejada possui {loja.estoqueBikes} bicletas, e você tentou alugar {bikes_a_alugar}"
            )
            self.alugarBikes(loja)

        except ValueError:
            print("Por favor, insira um dígito válido")
            self.alugarBikes(loja)

    def devolverBikes(self, agora):
        print(f"Você ficou com as bicicletas por {agora}")


# class LojadeBikes(object):
#     def __init__(self, nbicicletas):
#         # self.bikes será usado para representar quanto tempo falta para cada bike ficar disponível,
#         # então qnd um cliente alugar 3 bikes por 5 horas , 3 bikes com o value '0' terão um novo valor de 5 horas ,
#         # que será atualizado a cada hora(?)
#         self.nbikes = nbicicletas
#         self.money = 0
#         self.bikes = {
#             "bike1": 0,
#             "bike2": 0,
#             "bike3": 0,
#             "bike4": 0,
#             "bike5": 0,
#             "bike6": 0,
#             "bike7": 0,
#             "bike8": 0,
#             "bike9": 0,
#             "bike10": 0,
#             "bike11": 0,
#         }


# PEDRO AQUI ---------------------------------------


# CLASSE CLIENTE - DIRECIONAMENTO
# Ver as bicicletas disponíveis na Loja;
# Alugar bicicletas por hora (R$5/hora);
# Alugar bicicletas por dia (R$25/dia);
# Alugar bicicletas por semana (R$100/semana)
# Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos (de qualquer tipo) com 30% de desconto no valor total.

# class Cliente(object):
#     pass


# CLASSE LOJA - DIRECIONAMENTO
# Calcular a conta quando o cliente decidir devolver a bicicleta;
# Mostrar o estoque de bicicletas - DONE
# Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.


class Loja(object):
    def __init__(self, estoqueBikes):
        self.estoqueBikes = estoqueBikes
        self.caixa = 0
        self.precoHora = 10
        self.precoDia = 180
        self.precoSemana = 900

    # Mostrar o estoque de bicicletas

    def mostraEstoque(self):
        # fazer um print do estoque de bikes
        try:
            if self.estoqueBikes > 1:
                print(f"\nEstoque de Bicicletas - {self.estoqueBikes} bikes.")

            elif self.estoqueBikes == 1:
                print(f"\nEstoque de Bicicletas - {self.estoqueBikes} bike.")

            else:
                print(f"\nEstoque de Bicicletas - Vazio no momento.")
                return

        except:
            # raise na possibilidade do estoque ser negativo
            # levantar erros possíveis - ValueError e etc..
            pass

    # Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    # Calcular a conta quando o cliente decidir devolver a bicicleta;
    # SUPER FUNCAO KKK

    def valorTempoAluguelBikes(self, numeroBikes, tempoAluguel):
        while numeroBikes > self.estoqueBikes:
            print(
                "\nPedido recebido - Total de bikes não disponível no momento || Total bikes disponíveis no estoque: {self.estoqueBikes}."
            )
            validaAluguel = input(
                "Você ainda quer alugar alguma bike? Resp: Sim ou Não"
            )
            if validaAluguel.lower().strip() == "sim":
                numeroBikes = int(input(f"\nQuantas bikes você quer alugar? "))

            else:
                break
        # se o user digitar algo diferente de sim, ele sai da funcao e já era, caso nao, ele coloca um numero valido e segue
        # caso já nao tenha colocado um numeroBikes valido antes

        self.estoqueBikes -= numeroBikes

        # usar datetime aqui, apenas um exemplo de como seria
        try:
            if tempoAluguel == "hora":
                valorHora = "hora" * self.precoHora
                valorConta = numeroBikes * valorHora
                print(
                    "Pedido recebido - {numeroBikes} durante {tempoAluguel} hora/s, total de R$ {valorConta} reais, pedido confirmado || Total bikes disponíveis no estoque: {self.estoqueBikes}."
                )
                numeroBikesRecebidos = numeroBikes
                return True

            if tempoAluguel == "dia":
                valorDia = "dia" * self.precoDia
                valorConta = numeroBikes * valorDia
                print(
                    "Pedido recebido - {numeroBikes} durante {tempoAluguel} dia/s solicitadas, total de R$ {valorConta} reais, pedido confirmado || Total bikes disponíveis no estoque: {self.estoqueBikes}."
                )
                numeroBikesRecebidos = numeroBikes
                return True

            if tempoAluguel == "semana":
                valorSemana = "semana" * self.precoSemana
                valorConta = numeroBikes * valorSemana
                print(
                    "Pedido recebido - {numeroBikes} durante {tempoAluguel} semana/s solicitadas, total de R$ {valorConta} reais, pedido confirmado || Total bikes disponíveis no estoque: {self.estoqueBikes}."
                )
                numeroBikesRecebidos = numeroBikes
                return True

        except:
            pass


#eu = Cliente()
#lojinha = Loja(15)
#print("amor")

#momentoAluguel, nBikes = eu.alugarBikes(lojinha)
#print(momentoAluguel)


# eu.verificarBikes(lojinha)
# eu.alugarBikes(lojinha)

# Cada empréstimo segue apenas um modelo de cobrança (hora, dia ou semana);
# O cliente pode decidir livremente quantas bicicletas quer alugar;
# Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes disponíveis.
