import unittest
from datetime import timedelta
from LojaDeBikes import Loja, Cliente


class teste(unittest.TestCase):
    def setUp(self):
        self.Loja = Loja(15)
        self.cliente = Cliente()
        self.tempo = timedelta(days=5, hours=3, weeks=2)

    def testVerificarTempo(self):
        print("\n 1. Teste para verificar o tempo, onde ele foi inputado de maneira adequada")
        self.assertEqual(self.cliente.verificarTempo(2, "dias"), -1)

    def testVerificarTempoInadequado(self):
        print(
            "\n 1.1 Teste para verificar o tempo, onde ele foi inputado de maneira inadequada"
        )
        self.assertEqual(self.cliente.verificarTempo(2, "batata"), 0)

    def testVerificarTempoQntError(self):
        print("\n 1.2 Teste para verificar o tempo, onde ele foi inputado de maneira adequada")
        self.assertEqual(self.cliente.verificarTempo("50", "dias"), -1)

    def testAlugarBikes(self):
        print("\n 2. Teste Alugar 8 bikes, então não vai ter a promoção de familia ")
        self.assertEqual(
            self.cliente.alugarBikes(self.Loja, 8, "semanas"), (False, 8, "semanas")
        )

    def testAlugarBikesString(self):
        print("\n 2.1 Teste Alugar onde a quantidade de bikes não é um inteiro")
        self.assertEqual(self.cliente.alugarBikes(self.Loja, "8", "semanas"), 0)

    def testAlugarBikesQuantidadeNaoSuportada(self):
        print("\n 2.2 Teste Alugar onde a quantidade de bikes foi maior do que a disponível")
        self.assertEqual(self.cliente.alugarBikes(self.Loja, self.Loja.estoqueBikes+1, "dias"), -1),
    
    def testemostraEstoqueCerto(self):
        print('\n 3. Maneira correta de inserir o estoque, no setup')
        LojaTeste = Loja(15)
        self.assertEqual(LojaTeste.mostraEstoque(), -1)
    
    def testemostraEstoqueErrado(self):
        print('\n 3.1 Maneira incorreta de inserir o estoque, no setup')
        LojaTeste2 = Loja('batata')
        self.assertEqual(LojaTeste2.mostraEstoque(), 0)

    def testevalorTempoAluguelBikesCerto1(self):
        print('\n 4. Retorno correto para promo familia True')
        self.assertEqual(self.Loja.valorTempoAluguelBikes(8, "dias", self.tempo, True), -1)

    def testevalorTempoAluguelBikesCerto2(self):
        print('\n 4.1 Retorno correto para Promo familia False' )
        self.assertEqual(self.Loja.valorTempoAluguelBikes(8, "dias", self.tempo, False), -1)

    def testevalorTempoAluguelBikesPromoFamiliaCerto(self):
        print('\n 4.2 Retorno incorreto para Promo familia' )
        self.assertEqual(self.Loja.valorTempoAluguelBikes(8, "dias", self.tempo, 2), -2)

    def testevalorTempoAluguelBikesStempoCerto(self):
        print('\n 4.3 Retorno incorreto para o tipo de dado imputado no stempo')
        Tempo2 = 'banana'
        self.assertEqual(self.Loja.valorTempoAluguelBikes(8, Tempo2, self.tempo), -3)

    def testevalorTempoAluguelNumeroBikesCerto(self):
        print('\n 4.4 Retorno incorreto para número de bikes inválido' )
        self.assertEqual(self.Loja.valorTempoAluguelBikes('bananas', "dias", self.tempo, False), 0)

    def testevalorTempoAluguelBikesTempoCerto(self):
        print('\n 4.5 Retorno incorreto para tempo inválido' )
        self.assertEqual(self.Loja.valorTempoAluguelBikes(8, "semanas", 'bananas', False), -3)

    #def testevalorTempoAluguelBikesVazia(self):
    #    print('\n 4.5 Retorno incorreto para tempo inválido' )
    #    self.assertEqual(self.Loja.valorTempoAluguelBikes(), 0)

    # fazer teste time delta // numero bikes - colocar uns \n 

if __name__ == "__main__":
    unittest.main()
