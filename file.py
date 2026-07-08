# Function to calculate factorial
def calculate_factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get user input
number = 5
factorial_result = calculate_factorial(number)

print(f"The factorial of {number} is {factorial_result}")

