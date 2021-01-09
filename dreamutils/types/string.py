#!/usr/bin/python3

import re as _re
from typing import Union as _Union

"""This file contains utils for string manipulation"""


def remove_brackets(string: str) -> str:
    """
    Removes brackets and the content between it from a string

    Args:
        string: string from which the brackets should be removed

    Returns:
        `string` without brackets and the content between it

    Examples:
        >>> print(remove_brackets('This is [not] an example string (yuy)'))
        This is an example string

    """
    finished_string = ''
    square_brackets = 0
    parentheses = 0
    for brackets in string:
        if brackets == '[':
            square_brackets += 1
        elif brackets == '(':
            parentheses += 1
        elif brackets == ']' and square_brackets > 0:
            square_brackets -= 1
        elif brackets == ')' and parentheses > 0:
            parentheses -= 1
        elif square_brackets == 0 and parentheses == 0:
            finished_string += brackets

    return finished_string


def remove_space(string: str, space: _Union[str, int] = '  ', replace_with_single_space=True) -> str:
    """
    Removes all white space from `string` which is equal or higher than from the argument `space` given space

    Args:
        string: string from which the space should be removed
        space: Minimum size of the space to start the removal of white space in `string`
        replace_with_single_space: If True the space to remove is replaced with a single space instead of nothing

    Returns:
        `string` without the given space and higher

    Examples:
        >>> print(remove_space("This     string has  way to much        space"))
        This string has way to much space

    """
    if isinstance(space, int):
        space = ' ' * space

    space_to_replace = ''
    if replace_with_single_space:
        space_to_replace = ' '

    return _re.sub(space + '+', space_to_replace, string)
