import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

if __name__ == "__main__":
    unittest.main()


