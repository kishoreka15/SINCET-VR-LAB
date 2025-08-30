def factorial(n):
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Input from user
num = int(input("Enter a number to find its factorial: "))

# Calculate and print the factorial
result = factorial(num)
print(f"The factorial of {num} is {result}")
