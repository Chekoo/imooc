#coding=utf-8

from warnings import warn

class ReqStrSugRepr(type):
    def __int__(cls, name, bases, attrd):
        super(ReqStrSugRepr, cls).__init__(
            name, bases, attrd)
        if '__str__' not in attrd:
            raise TypeError("Class requires overriding of __str__()")
        if '__repr__' not in attrd:
            warn('Class suggests overriding of __repr__()\n', stacklevel=3)