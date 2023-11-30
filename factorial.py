
# Write a Python function to calculate the factorial of a non-negative integer.

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5
fact = factorial(num)
print(f"Factorial of {num} is {fact}")