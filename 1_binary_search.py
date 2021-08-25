from typing import Optional


def binary_search(sorted_list: list, searched_elem: int) -> Optional[int]:
    low_elem_idx = 0
    high_elem_idx = len(sorted_list) - 1

    while high_elem_idx >= low_elem_idx:
        middle_elem_idx = (low_elem_idx + high_elem_idx) // 2

        middle_elem = sorted_list[middle_elem_idx]
        if searched_elem == middle_elem:
            return middle_elem_idx
        elif searched_elem > middle_elem:
            low_elem_idx = middle_elem_idx + 1
        elif searched_elem < middle_elem:
            high_elem_idx = middle_elem_idx - 1

    return None


res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)
print("Test 1 Ok" if res == 5 else "Test 1 Failed")

res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1)
print("Test 2 Ok" if res is None else "Test 2 Failed")

res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
print("Test 3 Ok" if res is None else "Test 3 Failed")

res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
print("Test 4 Ok" if res == 0 else "Test 4 Failed")

res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
print("Test 5 Ok" if res == 9 else "Test 5 Failed")

res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 50)
print("Test 6 Ok" if res is None else "Test 6 Failed")

res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)
print("Test 7 Ok" if res == 8 else "Test 7 Failed")

res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
print("Test 8 Ok" if res == 1 else "Test 8 Failed")

res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
print("Test 9 Ok" if res == 3 else "Test 9 Failed")

res = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
print("Test 10 Ok" if res == 7 else "Test 10 Failed")
