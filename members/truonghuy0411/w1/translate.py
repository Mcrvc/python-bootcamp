def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Difference from C++:
    C++ requires nested loops and manual size allocation to transpose a matrix. 
    In contrast, Python achieves this in a single line using `zip(*matrix)`.
    """
    if not matrix or not matrix[0]:
        return []
        
    return [list(row) for row in zip(*matrix)]
