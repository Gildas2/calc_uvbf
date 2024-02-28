import unittest
from calculatrice import Calculatrice

class Testcalculatrice(unittest.TestCase):
    def test_addition(self):
        calc1 = Calculatrice(1, 2)
        self.assertEqual(calc1.addition(), 3)
        
        calc2 = Calculatrice(1.5, 2.5)
        self.assertTrue(calc2.addition() == 4)
     
    def test_mutiplication(self):
        calc1 = Calculatrice(2, 3)
        self.assertEqual(calc1.multiplication(), 6) 
        
        calc2 = Calculatrice(-2, 4)
        self.assertTrue(calc2.multiplication() == -8)
        
    def test_soustraction(self):
        calc1 = Calculatrice(6, 4)
        self.assertEqual(calc1.soustraction(), 2)    
        
        calc2 = Calculatrice(-4, 5)
        self.assertTrue(calc2.soustraction() == 1)
if __name__ == '__main__':
        unittest.main()