import unittest
from LojaDeBikes import Loja, Cliente

class teste(unittest.TestCase):
    def setUp(self):
        self.Loja = Loja(3)
        self.cliente = Cliente()

    def testVerificarTempo(self):
        print("Teste para verificar o tempo")
        self.assertEqual(self.cliente.verificarTempo("horas"), "horas")

if __name__ == "__main__":
    unittest.main()