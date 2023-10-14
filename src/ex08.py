"""
Execise 8
"""


def write_to_file(file, msg):
    """
    Write the given message to a file with the provided filename.

    Args:
        filename (str): The name of the file to write to.
        message (str): The message to write to the file.

    Returns:
        None
    """
    f=open(file,'w')
    f.write(msg)


def read_from_file(file):
    """
    Read the contents of a file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The contents of the file.
    """
    # TODO : complete this
    f=open(file,'r')
    return f.read()


def append_to_file(file, msg):
    """
    Append the given message to the end of the specified file.

    Args:
        filename (str): The name of the file to append the message to.
        message (str): The message to append to the file.

    Returns:
        None: This function does not return anything.
    """
    # TODO : complete this
    f=open(file,'a')
    f.write(msg)
