def fact(n: int):
    for el in range(1, n + 1):
        yield factorial(el)
print(n)