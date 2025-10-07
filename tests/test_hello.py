import unittest
from Hello import say_hello  # Import the function from Hello.py

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello from Python!")  # Check if the function returns the expected value

if __name__ == "__main__":
    unittest.main()  # Runs the test
