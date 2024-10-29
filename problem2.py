def factorial(n):
    multiplied = n
    while n > 0:
        n -= 1
        multiplied *= multiplied*n
    return multiplied
