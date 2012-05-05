# -*- coding: utf-8 -*-
import os


def _posix_home():
    return os.environ["HOME"]


def _nt_home():
    return os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"])


_systems = {
    'posix': _posix_home,
    'nt': _nt_home,
}


def path():
    get_home_path = _systems[os.name]
    return get_home_path()
