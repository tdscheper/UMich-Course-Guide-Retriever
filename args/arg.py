"""Define base class for a course guide argument."""
from args import _RawInputValue, _QueryKVPairs, _InputValue, _InputValues, \
                 _QueryValues, _ARG_TYPE_TO_QUERY_KEY
from args.meta_arg import MetaArg
from typing import final, Optional


class Arg(metaclass=MetaArg):
    """Base class for a Course Guide argument."""

    @final
    def __init__(self, input: Optional[_RawInputValue] = None) -> None:
        self._kvpairs: _QueryKVPairs = [] if not input else \
            type(self)._make_kvpairs(type(self)._translate_input_values(
                type(self)._fix_input_values(type(self)._prepare_input(
                    input
                ))
            ))
    
    @final
    @property
    def kvpairs(self) -> _QueryKVPairs:
        return self._kvpairs

    @final
    def url_piece(self) -> str:
        if type(self)._MANDATORY:
            assert self._is_set()
        
        if not self._is_set():
            return ''

        piece = ''
        for k, vals in self._kvpairs:
            piece += f'{k}='
            for v in vals:
                piece += f'{v}+'
            piece = piece[:-1] + '&'  # Remove last +, add &
        return piece[:-1]  # Remove last &
    
    @final
    def _is_set(self) -> bool:
        return bool(self._kvpairs)

    @classmethod
    def _valid_input_value(cls, input_value: _InputValue) -> bool:
        return cls._INPUT_VAL_TO_QUERY_VAL is None or \
            input_value in cls._INPUT_VAL_TO_QUERY_VAL
    
    @classmethod
    def _prepare_input(cls, input: _RawInputValue) -> _InputValues:
        return input.split(', ')
    
    @classmethod
    def _fix_input_values(cls, input_values: _InputValues) -> _InputValues:
        valids: _InputValues = []
        invalids: _InputValues = []

        for val in input_values:
            if cls._valid_input_value(val):
                valids.append(val)
            else:
                invalids.append(val)
        
        if invalids:
            cls._print_invalid_input_values_msg(invalids)

        return valids
    
    @classmethod
    def _translate_input_values(cls, input_values: _InputValues
        ) -> _QueryValues:
        if not cls._INPUT_VAL_TO_QUERY_VAL:
            return input_values
        return tuple([cls._INPUT_VAL_TO_QUERY_VAL[val] for val in input_values])

    @classmethod
    def _make_kvpairs(cls, query_values: _QueryValues) -> _QueryKVPairs:
        if not query_values:
            return set()
        
        # Most arguments map to query key and don't use + for values
        # key=v1&key=v2&...
        key = _ARG_TYPE_TO_QUERY_KEY[cls._ARGTYPE]
        return {(key, (v,)) for v in query_values}
    
    @classmethod
    def _print_invalid_input_values_msg(cls, invalids: _InputValues) -> None:
        if len(invalids) == 1:
            print(f"Not using invalid {cls._INPUT_KEY}: '{invalids[0]}'")
        else:
            print(f'Not using {len(invalids)} invalid {cls._INPUT_KEY}(s):')
            for inv in invalids:
                print(f"\t'{inv}'")
        
        cls._print_valid_input_values()
    
    @classmethod
    def _print_valid_input_values(cls) -> None:
        if not cls._INPUT_VAL_TO_QUERY_VAL:
            return

        print(f'Valid {cls._INPUT_KEY}(s):')
        for input_val in cls._INPUT_VAL_TO_QUERY_VAL:
            print(f'\t{input_val}')
