import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add1(self):
        self.assertEqual(self.calc.add(4, 5), 9)

    def test_add2(self):
        self.assertEqual(self.calc.add(5, 5), 10)

    def test_sub1(self):
        self.assertEqual(self.calc.subtract(5, 4), 1)

    def test_sub2(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_mul1(self):
        self.assertEqual(self.calc.multiply(5, 1), 5)

    def test_mul2(self):
        self.assertEqual(self.calc.multiply(12, 4), 48)

    def test_div1(self):
        self.assertEqual(self.calc.divide(12, 12), 1)

    def test_div2(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_mol1(self):
        self.assertEqual(self.calc.modulo(10, 10), 0)

    def test_mol2(self):
        self.assertEqual(self.calc.modulo(9, 2), 1)

if __name__ == '__main__':
    unittest.main()