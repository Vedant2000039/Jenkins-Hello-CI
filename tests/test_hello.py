import unittest
from Hello import greet, sum_numbers

class TestHello(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(), 30)

if __name__ == "__main__":
    unittest.main()
