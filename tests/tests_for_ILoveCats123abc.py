import pytest
from members.ILoveCats123abc.w1.translate import reverse_array

def test_reverse_even_elements():
    arr = [1, 2, 3, 4]
    assert reverse_array(arr) == [4, 3, 2, 1]

def test_reverse_odd_elements():
    arr = [1, 2, 3, 4, 5]
    assert reverse_array(arr) == [5, 4, 3, 2, 1]

def test_reverse_empty_array():
    arr = []
    assert reverse_array(arr) == []

def test_reverse_single_element():
    arr = [42]
    assert reverse_array(arr) == [42]

def test_reverse_with_negative_and_duplicates():
    arr = [-5, 2, 2, -10]
    assert reverse_array(arr) == [-10, 2, 2, -5]

def test_in_place_mutation():
    arr = [1, 2, 3]
    original_id = id(arr)
    result = reverse_array(arr)
    
    assert id(result) == original_id 
    assert arr == [3, 2, 1]           