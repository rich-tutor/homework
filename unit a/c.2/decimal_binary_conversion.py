def decimal_to_binary(decimal_num):
    """
    Convert a decimal number to a binary number.

    Args:
        decimal_num (int): The decimal number that needs to be converted.

    Returns:
        str: The binary representation of the input decimal number.

    Usage examples:
    >>> decimal_to_binary(10)
    '1010'
    >>> decimal_to_binary(15)
    '1111'
    """
    pass


def binary_to_decimal(binary_num):
    """
    Convert a binary number to a decimal number.

    Args:
        binary_num (str): The binary number that needs to be converted. The input should be a valid binary string containing only 0s and 1s.

    Returns:
        int: The decimal representation of the input binary number.

    Usage examples:
    >>> binary_to_decimal('1010')
    10
    >>> binary_to_decimal('1111')
    15
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()