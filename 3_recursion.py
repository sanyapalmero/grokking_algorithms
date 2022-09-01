def factorial(x: int) -> int:
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

print(factorial(5))
print(factorial(6))


def recursion_sum(arr: list) -> int:
    if len(arr) == 0:
        return 0
    
    first_elem = arr[0]
    arr.pop(0)
    return first_elem + recursion_sum(arr)


def recursion_sum2(arr: list) -> int:
    if len(arr) == 0:
        return 0
    
    return arr[0] + recursion_sum(arr[1:])


def recursion_sum2_inline(arr: list) -> int:
    return arr[0] + recursion_sum(arr[1:]) if len(arr) != 0 else 0


print(recursion_sum([2, 4, 6]))
print(recursion_sum2([2, 4, 6]))
print(recursion_sum2_inline([2, 4, 6]))
