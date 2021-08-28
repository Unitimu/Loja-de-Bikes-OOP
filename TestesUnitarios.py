import unittest
from LojaDeBikes import Loja, Cliente


class teste(unittest.TestCase):
    def setUp(self):
        self.Loja = Loja(15)
        self.cliente = Cliente()

    def testVerificarTempo(self):
        print("Teste para verificar o tempo, onde ele foi inputado de maneira adequada")
        self.assertEqual(self.cliente.verificarTempo(2, "dias"), -1)

    def testVerificarTempoInadequado(self):
        print(
            "Teste para verificar o tempo, onde ele foi inputado de maneira inadequada"
        )
        self.assertEqual(self.cliente.verificarTempo(2, "batata"), 0)

    def testVerificarTempoQntError(self):
        print("Teste para verificar o tempo, onde ele foi inputado de maneira adequada")
        self.assertEqual(self.cliente.verificarTempo("50", "dias"), -1)

    def testAlugarBikes(self):
        print("Teste Alugar 8 bikes, então não vai ter a promoção de familia ")
        self.assertEqual(
            self.cliente.alugarBikes(self.Loja, 8, "semanas"), (False, 8, "semanas")
        )

    def testAlugarBikesString(self):
        print("Teste Alugar onde a quantidade de bikes não é um inteiro")
        self.assertEqual(self.cliente.alugarBikes(self.Loja, "8", "semanas"), 0)

    def testAlugarBikesQuantidadeNaoSuportada(self):
        print("Teste Alugar onde a quantidade de bikes foi maior do que a disponível")
        self.assertEqual(self.cliente.alugarBikes(self.Loja, 50000, "dias"), -1)


if __name__ == "__main__":
    unittest.main()
