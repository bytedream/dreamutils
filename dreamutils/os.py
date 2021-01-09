#!/usr/bin/python3

import ctypes as _ctypes
import os as _os
from enum import Enum as _Enum
from sys import platform as _platform

"""This file contains utils for os manipulation"""


class Platform(_Enum):
    LINUX = 'linux'
    MAC = 'mac'
    WINDOWS = 'windows'
    OTHER = 'other'


def platform() -> Platform:
    """
    Returns the current platform / os

    Returns:
        Platform: The working platform / os

    Examples:
        >>> print(platform())
        Platform.LINUX

    """
    if _platform in ['linux', 'linux2']:
        return Platform.LINUX
    elif _platform == 'darwin':
        return Platform.MAC
    elif _platform in ['win32', 'cygwin', 'msys']:
        return Platform.WINDOWS
    else:
        return Platform.OTHER


def is_root() -> bool:
    """
    Checks if the python script is running with root / admin rights

    Notes:
        If the user who started the script is the root user on the system (e.g. pi on raspberry pi os)
        the script can execute root command even if it was not started with root rights

    Returns:
        If the script was started with root rights

    Examples:
        >>> print(is_root())
        False

    """
    if platform().LINUX or platform().MAC:
        return _os.geteuid() == 0
    elif platform().WINDOWS:
        return _ctypes.windll.shell32.IsUserAdmin() != 0
