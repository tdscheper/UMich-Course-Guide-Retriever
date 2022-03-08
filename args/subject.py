"""Define class for Subject argument."""
from args import _ArgType, _InputValue, _QueryValues, _QueryKVPairs, \
                 _ARG_TYPE_TO_QUERY_KEY
from args.meta_arg import MetaArg
from args.arg import Arg
from args.department import Department


class Subject(Arg, metaclass=MetaArg, argtype=_ArgType._SUBJECT):
    """Subject argument."""

    @classmethod
    def _valid_input_value(cls, input_value: _InputValue) -> bool:
        return Department._valid_input_value(input_value)
    
    @classmethod
    def _make_kvpairs(cls, query_values: _QueryValues) -> _QueryKVPairs:
        key = _ARG_TYPE_TO_QUERY_KEY[_ArgType._DEPARTMENT]
        return {(key, (v,)) for v in query_values}

    @classmethod
    def _print_valid_input_values(cls) -> None:
        print('Valid subjects look like EECS, SPANISH, etc.')
