"""Member 6"""
def reverse_array(arr: list[int]) -> list[int]:
    """
    Reverse a list/array in place and return it

    The difference between C++ and Python when solving the problem
    C++ needs temporary value or std::swap to swap 2 values in an array
    Python can swap with tuple-unpacking (arr[i], arr[j] = arr[j], arr[i])
    """
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr