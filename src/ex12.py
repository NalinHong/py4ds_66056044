"""
Execise 12
"""


def get_smallest(num_list):
    """
    Get the smallest number from a list of numbers.

    Args:
        num_list (list): A list of numbers.

    Returns:
        int or None: The smallest number from the list. If the list is empty, returns None.
    """
    if len(num_list) == 0:
        return None
    my_min = num_list[0]
    for i in num_list:
        if i < my_min:
            my_min = i
    return my_min
