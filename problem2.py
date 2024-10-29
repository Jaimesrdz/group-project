#This finds the factorial of a number
def factorial(n):
    multiplied = n
    while n > 1:
        n -= 1
        multiplied *= n
    return multiplied
print(factorial(5))