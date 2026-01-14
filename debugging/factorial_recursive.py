#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("factorial() not defined for negative numbers")

    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    num = int(sys.argv[1])
    print(factorial(num))
