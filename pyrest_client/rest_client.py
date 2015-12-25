# -*- coding: utf-8 -*-

import requests


"""
A simple rest client based on requests which gives users a way calling restful api in a chaining mode.
"""

__doc__ = 'A simple rest client based on requests which gives users a way calling restful api in a chaining mode.'


METHODS = ['get', 'head', 'post', 'patch', 'put', 'delete', 'options']


class _Executable(object):
    """
    Place where calls actually execute.
    """
    def __init__(self, method, path):
        self._method = method
        self._path = path

    @staticmethod
    def _make_request(url, method, **kwargs):
        return getattr(requests, method)(url, **kwargs)

    def __call__(self, **kw):
        return self._make_request(self._path, self._method, **kw)

    def __str__(self):
        return '_Executable (%s %s)' % (self._method, self._path)

    __repr__ = __str__


class _Callable(object):
    """
    Class for generating url in a chaining mode
    """
    def __init__(self, path):
        self._path = path

    def __getattr__(self, item):
        if item in METHODS:
            return _Executable(item, self._path)

        path = '%s/%s' % (self._path, item)
        return _Callable(path)

    def generate_url(self):
        return self._path

    def __str__(self):
        return '_Callable (%s)' % self._path

    __repr__ = __str__


class RestClient(object):
    """
    Entry point to start a call: RestClient('root_url').xxx.xxx.get(...)
    """
    def __init__(self, root_url=None):
        self._root_url = root_url

    def __getattr__(self, item):
        if '__' in item:
            return super(RestClient, self).__getattr__(item)

        return _Callable('%s/%s' % (self._root_url, item))
