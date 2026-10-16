from members.akagikay.w1.translate import insertion_sort


def test_normal_unsorted_list():
    inputList = [64, 34, 25, 12, 22, 11, 90]
    expectedList = [11, 12, 22, 25, 34, 64, 90]
    resultList = insertion_sort(inputList)

    assert resultList == expectedList


def test_already_sorted_and_reversed():
    sortedList = [1, 2, 3, 4, 5]
    assert insertion_sort(sortedList) == [1, 2, 3, 4, 5]

    reversedList = [5, 4, 3, 2, 1]
    assert insertion_sort(reversedList) == [1, 2, 3, 4, 5]


def test_empty_and_single_element():
    emptyList = []
    assert insertion_sort(emptyList) == []

    singleElementList = [42]
    assert insertion_sort(singleElementList) == [42]


def test_duplicate_elements():
    duplicateList = [4, 2, 4, 1, 2, 3, 1]
    assert insertion_sort(duplicateList) == [1, 1, 2, 2, 3, 4, 4]

    allSameList = [7, 7, 7, 7]
    assert insertion_sort(allSameList) == [7, 7, 7, 7]


def test_negative_numbers_and_zero():
    mixedList = [0, -10, 5, -3, 2, -1, 0, 8]
    expectedList = [-10, -3, -1, 0, 0, 2, 5, 8]
    assert insertion_sort(mixedList) == expectedList


def test_in_place_modification():
   
    originalList = [5, 1, 4, 2, 8]
    returnedList = insertion_sort(originalList)

    assert returnedList == [1, 2, 4, 5, 8]
    assert originalList == [1, 2, 4, 5, 8]
    assert returnedList is originalList