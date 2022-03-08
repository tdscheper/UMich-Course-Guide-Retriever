"""Define class for Course argument."""
from args import _ArgType, _InputValue, _RawInputValue, _InputValues, \
                 _QueryValues, _QueryKVPairs, _ARG_TYPE_TO_QUERY_KEY
from args.meta_arg import MetaArg
from args.arg import Arg
from args.department import Department
from args.catalog import Catalog


class Course(Arg, metaclass=MetaArg, argtype=_ArgType._COURSE):
    """Course argument."""
    _DEPARTMENT_QUERY_KEY = _ARG_TYPE_TO_QUERY_KEY[_ArgType._DEPARTMENT]
    _CATALOG_QUERY_KEY = _ARG_TYPE_TO_QUERY_KEY[_ArgType._CATALOG]

    @classmethod
    def _valid_input_value(cls, input_value: _InputValue) -> bool:
        input_value = input_value.split()
        return (
            len(input_value) == 2
            and Department._valid_input_value(input_value[0])
            and Catalog._valid_input_value(input_value[1])
        )
    
    @classmethod
    def _prepare_input(cls, input: _RawInputValue) -> _InputValues:
        return [input]
    
    @classmethod
    def _make_kvpairs(cls, query_values: _QueryValues) -> _QueryKVPairs:
        if not query_values:
            return set()
        
        dpt, cat = query_values[0].split()
        return {
            (cls._DEPARTMENT_QUERY_KEY, (dpt,)),
            (cls._CATALOG_QUERY_KEY   , (cat,))
        }
