"""
Exercise 15
"""


def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    input_sort = num_list
    input_sort.sort()
    input_len = len(num_list)
    if input_len == 0:
        return None
    elif input_len % 2 == 0:
        index = input_len//2
        return (input_sort[index]+input_sort[index-1])/2
    else:
        index = input_len//2
        return  input_sort[index]
