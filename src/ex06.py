"""
Execise 6
"""
"""
The ordinal suffix depends on the last two digits in the number:
    * If the last two digits end with 11, 12, or 13 then the suffix is ―th.
    * If the number ends with 1, the suffix is ―st.
    * If the number ends with 2, the suffix is ―nd.
    * If the number ends with 3, the suffix is ―rd.
    * Every other number has a suffix of ―th.
"""

def ordinal_suffix(param):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # TODO : complete this
    if param%100 ==11 or param%100 ==12 or param%100 ==13:
        return str(param)+'th'
    elif param%10 ==1:
        return str(param)+'st'
    elif param%10==2:
        return str(param)+'nd'
    elif param%10==3:
        return str(param)+'rd'
    else:
        return str(param)+'th'


#%%
