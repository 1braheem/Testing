def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Iterative: {num}! = {factorial_iterative(num)}")
            print(f"Recursive: {num}! = {factorial_recursive(num)}")
    except ValueError:
        print("Please enter a valid integer.")
