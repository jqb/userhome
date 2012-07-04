# -*- coding: utf-8 -*-
import os
from os import path as ospath


def _posix_home(*path):
    """
    Create paths starting with current user home directory.
    This version works properly only for POSIX systems.

    Assuming, you're login on the system as "jacob",
    usage looks like this::

       >>> import userhome
       >>> userhome._posix_home() == '/home/jacob/'
       >>> userhome._posix_home(".templates") == '/home/jacob/.templates'
       >>> userhome._posix_home(".templates", "django") == '/home/jacob/.templates/django'
    """
    return ospath.join(os.environ["HOME"], *path)


def _nt_home(*path):
    """
    Create paths starting with current user home directory.
    This version works properly only for NT systems.

    Assuming, you're login on the system as "jacob",
    usage looks like this::

       >>> import userhome
       >>> userhome._nt_home() == 'C:\\Users\\jacob'
       >>> userhome._nt_home(".templates") == 'C:\\Users\\jacob\\.templates'
       >>> userhome._nt_home(".templates", "django") == 'C:\\Users\\jacob\\.templates\\django'

    """
    return ospath.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], *path)


_systems = {
    'posix': _posix_home,
    'nt': _nt_home,
}


def path(*path):
    get_home_path = _systems[os.name]
    return get_home_path(*path)
