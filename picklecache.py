#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""

import os
import pickle


class PickleCache(object):
    """Class Docstring"""
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor"""
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """SetItem function"""
        self.__data[key] = value

    def __len__(self):
        """Gets len"""
        return len(self.__data)

    def __getitem__(self, key):
        """Get item function"""
        if self.autosync is True:
            self.flush()
            self.__delitem__(key)
        try:
            return self.__data[key]
        except (TypeError, KeyError):
            raise

    def __delitem__(self, key):
        """Deletes Item"""
        del self.__data[key]

    def load(self):
        """Loads item"""
        if (os.path.exists(self.__file_path)
           and os.path.getsize(self.__file_path) != 0):
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """Flush function"""
        fhandler = open(self.__file_path, 'wb')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
