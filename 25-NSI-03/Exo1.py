def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))