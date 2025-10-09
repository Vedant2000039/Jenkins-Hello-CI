# Hello.py
import os

def greet():
    return "Hello, World!"

def sum_numbers(x, y):
    return x + y

if __name__ == "__main__":
    # Read parameters passed by Jenkins (use defaults if not set)
    x = int(os.getenv("X_VALUE", 10))
    y = int(os.getenv("Y_VALUE", 20))

    print(greet())
    print(f"Sum is: {sum_numbers(x, y)}")
