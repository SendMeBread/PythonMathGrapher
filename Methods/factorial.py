def factorial(n):
    loop = n
    result = n
    while loop > 1:
        result *= n - 1
        loop -= 1
        n -= 1
    return result
