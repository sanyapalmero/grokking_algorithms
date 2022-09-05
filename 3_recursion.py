from operator import le


def factorial(x: int) -> int:
    """Вычисляет факториал для числа x"""
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

print(factorial(5))
print(factorial(6))

# ----------------------------------------- 

def recursion_sum(arr: list) -> int:
    """Рекурсивная функция для подсчёта суммы элементов массива"""
    if len(arr) == 0:
        return 0
    
    # Из массива достается первый элемент, 
    first_elem = arr[0]

    # Затем этот первый элемент удаляется из массива
    arr.pop(0)

    # И первый элемент массива суммируется с результатом рекурсивной функции
    # В рекурсивную функцию передается массив уже без первого элемента
    # И так до тех пор, пока массив не станет пустым 
    return first_elem + recursion_sum(arr)


def recursion_sum2(arr: list) -> int:
    """Рекурсивная функция для подсчёта суммы элементов массива (Версия 2)"""
    if len(arr) == 0:
        return 0
    
    # Тоже самое, только здесь используются срезы вместо .pop()
    return arr[0] + recursion_sum(arr[1:])


def recursion_sum2_inline(arr: list) -> int:
    return arr[0] + recursion_sum(arr[1:]) if len(arr) != 0 else 0


print(recursion_sum([2, 4, 6]))
print(recursion_sum2([2, 4, 6]))
print(recursion_sum2_inline([2, 4, 6]))

# ----------------------------------------- 

def recursion_array_len(arr: list, cnt: int = 0) -> int:
    """Рекурсивная функция подсчёта числа элементов в массиве"""
    if not arr:
        return cnt
    return recursion_array_len(arr[1:], cnt + 1)

print(recursion_array_len([]))
print(recursion_array_len([2]))
print(recursion_array_len([2, 4, 6, 4]))


def recursion_array_len_v2(arr: list) -> int:
    """Рекурсивная функция подсчёта числа элементов в массиве (без использования второго аргумента)"""
    if not arr:
        return 0
    return 1 + recursion_array_len_v2(arr[1:])
    

print(recursion_array_len_v2([]))
print(recursion_array_len_v2([2]))
print(recursion_array_len_v2([2, 4, 6, 4]))
