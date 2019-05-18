def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    N = len(input_list)

    if N <= 1:
        return -1, -1

    digits_freq = [0] * 10
    for digit in input_list:
        digits_freq[digit] += 1

    m1 = ''
    m2 = ''
    gate = 1 if N % 2 == 0 else 2

    for i in range(9, -1, -1):
        while digits_freq[i]:
            if gate:
                m1 += str(i)
                gate -= 1
            else:
                m2 += str(i)
                gate += 1
            digits_freq[i] -= 1
    return int(m1), int(m2)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
