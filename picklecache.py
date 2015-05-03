#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""

import os
import pickle

class PickleCache():
    def __init__(self, file_path='datastore.pkl', autosync=False):
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        
        
    def __setitem__(self, key, value):
        
        self.__data[key] = value
        
    def __len__(self):
        return len(self.__data)

    def __getitem__(self, key):
        try:
            return self.__data[key]
        except (TypeError, KeyError):
            raise KeyError

    def __delitem__(self, key):
        del self.__data[key]

    def load(self):
        if (os.path.exists(self.__file_path)
            and os.path.getsize(self.__file_path) != 0):
            self.__data = pickle.load(self.__file_path)
            close(self.__file_path)
            
            
