def get_small_idx(arr: list) -> int:
    small_elem = arr[0]
    small_elem_idx = 0
    
    for i in range(1, len(arr)):
        current_elem = arr[i]
        if current_elem < small_elem:
            small_elem_idx = i
            small_elem = current_elem
    
    return small_elem_idx


def selection_sort(arr: list) -> list:
    sorted_arr = []

    for _ in range(len(arr)):
        small_idx = get_small_idx(arr)
        small_elem = arr.pop(small_idx)
        sorted_arr.append(small_elem)

    return sorted_arr


def selection_sort_v2(arr: list) -> list:
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def main():
    sorted_arr = selection_sort([5, 3, 6, 2, 10, 7])
    print(sorted_arr)

    sorted_arr2 = selection_sort_v2([5, 3, 6, 2, 10, 7])
    print(sorted_arr2)

main()
