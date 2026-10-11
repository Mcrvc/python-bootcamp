"""Member 1"""
def binary_search(a: list[int], key: int) -> int:
    """
    Return the index of key in sorted list a, or -1 if not found.

    Python lists are flexible and can hold different types of data. 
    Because of this, you don't need complex type declarations 
    like const std::vector<int>& or type casts like (int)a.size(). 
    You can just use len(a) to get an integer, and the loop logic naturally handles array bounds
    """
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == key:
            return mid
        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
