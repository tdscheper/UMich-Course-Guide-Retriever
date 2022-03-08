"""Metaclass for an argument."""
from args import _ArgType, _InputKey, _InputValue, _QueryValue, \
                 _ARG_TYPE_TO_INPUT_KEY, _ARG_TYPE_TO_INPUT_VAL_TO_QUERY_VAL, \
                 _ARG_TYPE_TO_DEFAULT_INPUT_VALUE
from typing import Optional as Opt, Dict


class MetaArg(type):
    """Dynamically create an argument class."""

    def __new__(cls, name, bases, namespace, **kwargs):
        return super().__new__(cls, name, bases, namespace)
    
    def __init__(cls, name, bases, namespace, argtype: Opt[_ArgType] = None, 
                 mandatory: bool = False, **kwargs):
        cls._ARGTYPE: Opt[_ArgType] = argtype

        # True if argument must be present in query
        cls._MANDATORY: bool = mandatory

        cls._INPUT_KEY: Opt[_InputKey] = \
            _ARG_TYPE_TO_INPUT_KEY.get(cls._ARGTYPE, None)
        
        cls._INPUT_VAL_TO_QUERY_VAL: Opt[Dict[_InputValue, _QueryValue]] = \
            _ARG_TYPE_TO_INPUT_VAL_TO_QUERY_VAL.get(cls._ARGTYPE, None)
        
        cls._DEFAULT_INPUT_VALUE: Opt[_InputValue] = \
            _ARG_TYPE_TO_DEFAULT_INPUT_VALUE.get(cls._ARGTYPE, None)

        super().__init__(name, bases, namespace)
