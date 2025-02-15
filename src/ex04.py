"""
Execise 4
"""
#1. area = L x W
#2. perimeter = L+W + L+W
#3. volume = L x W x H
#4. surface area = 2 x (L x W) + 2 x (W x H) + 2 x (L x H)

def area(param1, param2):
    """
    Calculates the area of a rectangle given its length and width.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    # TODO : complete this
    return param1*param2


def perimeter(param1, param2):
    """
    Calculate the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    # TODO : complete this
    return param1+param2+param1+param2


def volume(param1, param2, param3):
    """
    Calculates the volume of an object given its length, width, and height.

    Args:
        length (float): The length of the object.
        width (float): The width of the object.
        height (float): The height of the object.

    Returns:
        float: The volume of the object.
    """
    # TODO : complete this
    return param1*param2*param3


def surface_area(param1, param2, param3):
    """
    Calculate the surface area of a rectangular prism.

    Parameters:
        length (float): The length of the rectangular prism.
        width (float): The width of the rectangular prism.
        height (float): The height of the rectangular prism.

    Returns:
        float: The total surface area of the rectangular prism.
    """
    # TODO : complete this
    return 2*(param1*param2)+2*(param2*param3)+2*(param1*param3)
