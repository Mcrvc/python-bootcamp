# Calculate the sum of every integer in a number (value)

def sum_of_int(value: int) -> int:
    value = abs(value)
    answer = 0
    while value != 0:
        answer += value % 10
        value = value // 10
    return answer

"""
Note: Unlike C++, where integer division implicitly truncates the fractional component, Python's / operator evaluates to a float. We must use // to enforce floor division.
"""