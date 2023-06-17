def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start_index = 0
    end_index = len(input_list) - 1
    pivot = input_list[0]

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if input_list[mid_index] == max(input_list[mid_index], input_list[mid_index - 1], input_list[mid_index + 1]):
            max_num_index = mid_index
            break
        elif input_list[mid_index + 1] == max(input_list[mid_index], input_list[mid_index - 1], input_list[mid_index + 1]):
            if input_list[mid_index] < pivot:
                end_index = mid_index
            else:
                start_index = mid_index + 1
        else:
            max_num_index = mid_index - 1
            break

    if number > input_list[max_num_index] or number < input_list[max_num_index + 1]:
        return - 1

    if number >= pivot:
        index = search_func(input_list[:max_num_index + 1], number)
        return index if index != -1 else -1
    else:
        index = search_func(input_list[max_num_index + 1:], number)
        return (max_num_index + 1 + index) if index != -1 else -1

def search_func(array, target):
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)

def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    if array[mid_index] == target:
        return mid_index
    elif array[mid_index] < target:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)
    else:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)

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
