def factorial(x: int) -> int:
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

print(factorial(5))
print(factorial(6))
