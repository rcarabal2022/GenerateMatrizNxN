import unittest
from generatematrix import enterN

class TestnMatrix(unittest.TestCase):
    def test_nmatrix(self):
        print(' Prueba de valores de resultado conocido')
        self.assertEqual(enterN(True,0),3)

if __name__ == '__main__':
    unittest.main()
        