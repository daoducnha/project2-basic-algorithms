def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    arr_rs = [*range(1, number, 1)]
    return sqrt_func(number, arr_rs)

def sqrt_func(number, arr):
    if number == 0 or number == 1:
        return number

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if (arr[mid] * arr[mid]) == number:
            return arr[mid]
        elif (arr[mid] * arr[mid]) < number:
            start = mid + 1
            rs = arr[mid]
        else:
            end = mid - 1
    return rs

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")