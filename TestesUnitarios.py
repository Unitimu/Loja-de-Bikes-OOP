import unittest
from LojaDeBikes import Loja, Cliente

class teste(unittest.TestCase):
    def setUp(self):
        self.Loja =Loja(3, 10)
        self.cliente = Cliente()

    

