import heapq
import math


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    heap = []
    for i in input_list:
        heapq.heappush(heap, i)

    num1 = 0
    num2 = 0
    base = 10
    i = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        num1 += first * math.pow(base, i)
        num2 += second * math.pow(base, i)
        i += 1

    if len(heap) == 1:
        num2 += heapq.heappop(heap) * math.pow(base, i)

    return [num2, num1]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)