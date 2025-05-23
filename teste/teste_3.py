#TESTE UNITARIO
# Função pura (sem dependências externas)
def calcular_desconto(valor, porcentagem):
    if not 0 <= porcentagem <= 100:
        raise ValueError("Porcentagem inválida")
    return valor * (1 - porcentagem/100)

# Teste unitário com unittest
import unittest

class TestDesconto(unittest.TestCase):
    def test_desconto_valido(self):
        self.assertEqual(calcular_desconto(100, 10), 90)
    
    def test_desconto_zero(self):
        self.assertEqual(calcular_desconto(200, 0), 200)
    
    def test_erro_porcentagem_invalida(self):
        with self.assertRaises(ValueError):
            calcular_desconto(50, 110)

# Executar no Colab
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
