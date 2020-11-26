#!/usr/bin/python3

import socket as _socket

from json import load as _load
from urllib.request import urlopen as _urlopen

"""This file contains utils for networking stuff"""


def online(timeout=5) -> bool:
    """
    Tests if your machine is connected to the internet

    Args:
        timeout (optional): Timeout until False is returned if no connection can be established

    Returns:
        If the pc is online (theoretically it could return False when google.com is down, but if this happens your connect status is the smallest problem)

    Examples:
        >>> print(online(2))
        True

    """
    try:
        host = _socket.gethostbyname('google.com')

        connection = _socket.create_connection((host, 80), timeout)
        connection.close()

        return True
    except:
        return False


def get_ip_infos(ip_address: str = None) -> dict:
    """
    A dict with infos about the ip address of your computer (unless you use a vpn) or a specified ip

    Args:
        ip_address (optional): IP from which you want to receive the information

    Returns:
        A dict filled with the ip address information

    Examples:
        >>> print(get_ip_infos()())
        {'ip': '69.69.69.69',
         'hostname': 'examplehostname',
         'city': 'Suginami City',
         'region': 'Tokyo',
         'country': 'JP,
         'loc': '35.6986, 139.6367',
         'org': 'exampleprovider',
         'postal': '166-0015',
         'timezone': 'Asia/Tokyo',
         'readme': 'https://ipinfo.io/missingauth'}

    """
    if ip_address:
        return _load(_urlopen('http://ipinfo.io/' + ip_address + '/json'))
    else:
        return _load(_urlopen('http://ipinfo.io/json'))
