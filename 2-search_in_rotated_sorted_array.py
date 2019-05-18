def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    N = len(input_list)

    pivot = find_pivot(input_list, 0, N-1)

    if pivot == -1:
        print('No pivot')
    if input_list[pivot] == number:
        return pivot

    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot-1, number)
    return binary_search(input_list, pivot+1, N-1, number)

def binary_search(input_list, start, end, number):
    if start > end:
        return -1

    mid = int((start + end) / 2)

    if input_list[mid] == number:
        return mid
    if input_list[mid] < number:
        return binary_search(input_list, mid + 1, end, number)
    if input_list[mid] > number:
        return binary_search(input_list, start, mid - 1, number)

def find_pivot(input_list, start, end):
    if start > end:
        return -1
    if start == end:
        return start

    mid = int((start + end) / 2)

    if mid < end and input_list[mid] > input_list[mid + 1]:
        return mid
    if mid > start and input_list[mid] < input_list[mid - 1]:
        return mid - 1
    if input_list[start] >= input_list[mid]:
        return find_pivot(input_list, start, mid - 1)
    return find_pivot(input_list, mid + 1, end)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
