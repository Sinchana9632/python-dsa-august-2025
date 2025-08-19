"""
📌 Program: Find Factorial of a Number
📌 Date: 2025-08-16
📌 Author: sinchana
"""

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ✅ Example Test
if __name__ == "__main__":
    number = 5
    print(f"Factorial of {number} = {factorial(number)}")
