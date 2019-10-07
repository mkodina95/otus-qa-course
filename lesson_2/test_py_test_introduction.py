

# Pythagorean theorem
def test_1(some_numbers):
    """
    This test contains the formula for the Pythagorean theorem (c^2=a^2 + b^2)
    The result should be calculated correctly
    """
    values = some_numbers
    c = ((values[0] ** 2) + (values[1] ** 2)) ** (1 / 2)
    assert (c == 5)


# Remainder of division
def test_2(some_numbers):
    """
    This test contains the formula of calculating of the integer remainder of division
    The result should be calculated correctly
    """
    values = some_numbers
    res = values[0] % values[1]
    assert (res == 1)


# Length of the array
def test_3():
    """
    This test contains the list with different types of data
    The result should calculate the correct length of the list
    """
    arr_different_types = [1, 3, 'hi', {'key': "value"}, (1, 2, 3), None, 5.3]
    arr_length = len(arr_different_types)
    assert (arr_length == 7)


# Hello, world
def test_4():
    """
    This test contains the two strings
    The result should have the correct addition of two strings
    """
    str1 = "Hello,"
    str2 = " world"
    res = str1 + str2
    assert (res == "Hello, world")


# Array join
def test_5():
    """
    This test contains the list of symbols
    The result should join the symbols to one string
    """
    arr_of_symbols = ['M', 'y', ' ', 'l', 'i', 't', 't', 'l', 'e', ' ', 'P', 'o', 'n', 'y']
    res = "".join(arr_of_symbols)
    assert (res == "My little Pony")


# Compare tuple element
def test_6():
    """
    This test contains the tuple with 5 elements
    The result should perform the correct element in the tuple
    """
    tuple_colours = ('red', 'orange', 'yellow', 'green', 'blue')
    tuple_element = tuple_colours[3]
    assert (tuple_element == 'green')


# Length of dictionary
def test_7():
    """
    This test contains two dictionaries, which should be added to the new dictionary
    The result should calculate the correct length of the new dictionary
    """
    dict_weekdays = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}
    dict_weekends = {6: 'Saturday', 7: 'Sunday'}
    dict_week = {}
    dict_week.update(dict_weekdays)
    dict_week.update(dict_weekends)
    assert (len(dict_week) == 7)


# Intersections of sets
def test_8():
    """
    This test contains two sets with elements, the common elements of these sets will be added to the new set
    The result should be the set with the common element
    """
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    set_c = set_a.intersection(set_b)
    assert (set_c == {3})


# Comparison of the reversed word
def test_9():
    """
    This test contains the string, which will be reversed
    the result should be the reversed string
    """
    str_1 = 'Introduction'
    reversed_str = str_1[::-1]
    assert (reversed_str == 'noitcudortnI')


# Entering the set
def test_10():
    """
    This test contains two sets with elements, which are compared
    The result should be the boolean, which depicts if the second set is subset of the first set
    """
    set_symbols = set('this is the homework')
    set_subset = {'w', 'o', 'r', 'k'}
    result = set_subset.issubset(set_symbols)
    assert (result is True)

