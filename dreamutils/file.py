#!/usr/bin/python3

import os as _os
from typing import Generator as _Generator, List as _List, Union as _Union

"""This file contains utils for file manipulation"""


def recursive_directory_data(directory: str, full_path=True) -> _Generator[str]:
    """
    _Lists every subfile and subdirectory of the given directory

    Args:
        directory (str): Path of directory from which you want to get the subfiles /- directories
        full_path (bool, optional): If True the full path of the files gets returned. If False the relative path

    Yields:
        str: The next recursive file or directory in the given directory

    Examples:
        >>> print(recursive_directory_data('/home/ByteDream/NOTHENTAI'))
        ['/home/ByteDream/NOTHENTAI/download_1.mp4', '/home/ByteDream/NOTHENTAI/best/', '/home/ByteDream/NOTHENTAI/best/best_1.mp4']

    """
    if directory.endswith(_os.sep):
        directory = directory[:-1]

    for path, subdirs, files in _os.walk(directory):
        if full_path:
            yield _os.path.join(path, _os.sep.join(subdirs))
        else:
            if path.endswith(_os.sep):
                path = path[:path.rfind(_os.sep)]
            yield path[path.rfind(_os.sep) + 1:]
        for name in files:
            if full_path:
                yield _os.path.join(path, name)
            else:
                yield _os.path.join(path.replace(directory, ''), name)


def replace_line(file: str, to_replace: _Union[int, str, _List[int], _List[str]], new_content: str, ignore_case=False) -> None:
    """
    Replaces lines given by their number or content with new content

    Args:
        file: File in which the lines are to be replaced
        to_replace: Content like line numbers or line content which should be replaced
        new_content: New content to replace the old one
        ignore_case: If True and `to_replace` is a string or a _List of strings, the comparison is not case sensitive

    Examples:
        test.txt before:
        ```
        line 1
        line 2
        line 3
        line 4
        ```

        >>> replace_line('test.txt', 'line 3', 'replaced line 3')

        test.txt after:
        ```
        line 1
        line 2
        replaced line 3
        line 4
        ```

    """
    lines = open(file, 'r').readlines()

    if isinstance(to_replace, str):
        to_replace = [to_replace]

    if ignore_case:
        for index, item in enumerate(to_replace):
            to_replace[index] = item.lower()

    if isinstance(to_replace, int):
        lines[to_replace] = new_content
    elif to_replace:
        if isinstance(to_replace[0], int):
            for index, _ in enumerate(lines.copy()):
                if index in to_replace:
                    lines[index] = new_content
                    to_replace.remove(index)
        else:
            for index, item in enumerate(lines.copy()):
                if ignore_case:
                    item = item.lower()
                if item in to_replace:
                    lines[index] = new_content

    with open(file, 'w') as file:
        file.writelines(lines)
        file.cl_ose()
