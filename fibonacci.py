"""
Program: Fibonacci Series
 Date: 2025-08-16
 Author: sinchana """

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Test
fibonacci(10)
