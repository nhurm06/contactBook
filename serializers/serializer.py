#!/usr/bin/env python3
'''
Serialization Base class

'''
from abc import abstractmethod

class Serializer(object):
    '''
    Base Class designed to unify serialization and disk access
    '''
    _format = None ##private variable to allow dynamic population of supported formats

    def __int__(self):
        self._file = None

    def __new__(cls, format):
        '''
        Allows us to call the sub classes based on the ._format attribute
        :param format: str
        :return: Serializer sub class
        '''
        subclass_map = {subclass.getFormat(): subclass for subclass in cls.__subclasses__()}
        subclass = subclass_map[format]
        instance = super(Serializer, subclass).__new__(subclass)
        return instance
    def open(self,path):
        f = open(path,newline="")
        self._file = f
        return self._file

    def read(self, path):
        '''
        Base function for reading files from disk
        :param path: str
        :return:
        '''
        self._file = self.open(path)
        return self._file.read()

    def close(self):
        '''
        Close any open file handles
        :return: None
        '''
        if self._file:
            self._file.close()
        self._file = None

    @abstractmethod
    def decode(self,data):
        '''
        Abstract method for each subclass. This is where we're use format
        specific logic
        :param data:
        :return:
        '''
        pass
    @abstractmethod
    def encode(self,data):
        '''
        Abstract method for each subclass. This is where we're use format
        specific logic
        :param data:
        :return:
        '''
        pass
    def write(self, path, data):
        '''
        Write the serialized data to disk
        :param path: str
        :param data: dict
        :return: file
        '''
        with open(path,"w") as f:
            f.write(self.encode(data))
    @classmethod
    def getFormat(cls):
        '''
        Class method to allow functions to access the sub class
        :return: str
        '''
        return cls._format

    @classmethod
    def queryFormats(cls):
        '''
        Class method to dynamically return all sub classes to show users which formats are available
        :return: list
        '''
        return ([x.getFormat() for x in cls.__subclasses__()])