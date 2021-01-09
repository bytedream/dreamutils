#!/usr/bin/python3


def index(dictionary: dict, index: int):
    """
    Index a dictionary

    Args:
        dictionary: Dictionary to index
        index: Position of value to index

    Returns:
        The indexed value

    Raises:
        IndexError: If the dictionary index is out of range

    """

    try:
        return list(dictionary)[index]
    except IndexError:
        raise IndexError('dict index out of range')  # just replacing 'list' with 'dict' in the error message


def index_by_value(dictionary: dict, value):
    """
    Index a dictionary by a value of it

    Args:
        dictionary: Dictionary to index
        value: Value to index

    Returns:
        The indexed key

    Raises:
        IndexError: If the given value is not in the dictionary

    """
    try:
        return list(dictionary.keys())[list(dictionary.values()).index(value)]
    except ValueError:
        raise IndexError('dict value index out of range')
