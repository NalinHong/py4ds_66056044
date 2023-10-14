"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    result = ''
    my_sec = tsec % 60
    my_min =(tsec // 60) % 60
    my_hour = tsec//3600
    if tsec == 0: return '0s'
    if my_sec > 0:
        result = str(my_sec)+'s '
    if my_min > 0:
        result = str(my_min)+'m '+result
    if my_hour > 0:
        result = str(my_hour) + 'h ' +result
    return result.strip()

#%%
