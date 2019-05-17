def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start = 0
    end = number
    return sqrt_binary_search(start, end, number)

def sqrt_binary_search(start, end, number):
    mid = int((start + end) / 2)
    if start > end:
        return mid
    if mid * mid == number:
        return mid
    elif mid * mid < number:
        return sqrt_binary_search(mid + 1, end, number)
    else:
        return sqrt_binary_search(start, mid - 1, number)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")