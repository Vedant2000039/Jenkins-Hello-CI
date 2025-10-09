import unittest
from Hello import greet, sum_numbers

class TestHello(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(10, 20), 30)
        self.assertEqual(sum_numbers(-5, 5), 0)
        self.assertEqual(sum_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
