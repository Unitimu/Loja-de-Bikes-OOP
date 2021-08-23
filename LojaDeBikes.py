import datetime

class Cliente(object):
    def verificarBikes(self,loja):
        print(loja.nbikes)

    def alugarBikes(self,loja):
        try :
            bikes_a_alugar = int(input('Quantas bicicletas você deseja alugar? '))

            if bikes_a_alugar == 0:
                raise ValueError
            if bikes_a_alugar>= loja.nbikes:
                raise SystemError('A loja não tem essa quantidade de bibicletas disponível no momento')

            ntempo, stempo = input(f'Por quanto tempo deseja alugar {bikes_a_alugar} bicletas? (Ex:"6 horas"/"3 dias"/"2 semanas")').split()
            ntempo = int(ntempo)

            if stempo not in 'horasdiassemanas':
                raise NameError

            # if stempo in 'horas':
            #     print('joquei, GUIGUI')
            #     print('Pedro, GUILHERME ')



        except SystemError:
            print(f'A loja desejada possui {loja.nbikes} bicletas, e você tentou alugar {bikes_a_alugar}')
            # self.alugarBikes()

        except NameError:
            print(f'O sistema não reconhece o termo "{stempo}", por favor insira o formato do tempo desejado como: "horas","dias" ou "semanas" ')


        except :
            print('Por favor, insira um dígito válido')
            # self.alugarBikes()

        


class LojadeBikes(object):
    def __init__(self,nbicicletas):
        # self.bikes será usado para representar quanto tempo falta para cada bike ficar disponível,
        # então qnd um cliente alugar 3 bikes por 5 horas , 3 bikes com o value '0' terão um novo valor de 5 horas ,
        # que será atualizado a cada hora(?)
        self.nbikes = nbicicletas
        self.money = 0
        self.bikes = {
            'bike1' : 0,
            'bike2' : 0,
            'bike3' : 0,
            'bike4' : 0,
            'bike5' : 0,
            'bike6' : 0,
            'bike7' : 0,
            'bike8' : 0,
            'bike9' : 0,
            'bike10' : 0,
            'bike11' : 0,


        }

eu = Cliente()
lojinha = LojadeBikes(15)

eu.verificarBicicletas(lojinha)

print('bananas')

