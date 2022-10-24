def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


assert quick_sort([2, 1, 7, 0, 5, 4]) == [0, 1, 2, 4, 5, 7]


def quick_sort2(arr: list) -> list:
    if len(arr) < 2:
        return arr

    pivot = arr[(0 + (len(arr) - 1)) // 2]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort2(less) + [pivot] + quick_sort2(greater)


print(quick_sort2([2, 1, 7, 0, 5, 4]))
assert quick_sort2([2, 1, 7, 0, 5, 4]) == [0, 1, 2, 4, 5, 7]

