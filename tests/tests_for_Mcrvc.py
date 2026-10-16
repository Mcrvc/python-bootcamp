from members.Mcrvc.w1.translate import  binary_search


def test_normal_list():
    inputList = [1,2,3,4,5,6,7,8,9,10]
    assert (binary_search(inputList, 5) == 4)

def test_empty_list():
    inputList = []
    assert (binary_search(inputList, 0) == -1)

def test_key_at_start():
    inputList = [1,2,3,4,5,6,7,8,9,10]
    assert binary_search(inputList, 0) == -1

def test_key_at_end():
    inputList = [1,2,3,4,5,6,7,8,9,10]
    assert binary_search(inputList, 0) == -1

def test_key_at_middle():
    inputList = [1,2,3,4,5,6,7,8,9,10]
    assert binary_search(inputList, 6) == 5

def test_key_at_middle2():
    inputList = [1,2,3,4,5,6,7,8,9,10]
    assert binary_search(inputList, 5) == 4