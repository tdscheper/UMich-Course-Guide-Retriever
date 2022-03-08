"""Define class for Meeting Time argument."""
from args import _ArgType, _InputValue, _RawInputValue, _InputValues, \
                 _QueryValues, _QueryKVPairs, _ARG_TYPE_TO_QUERY_KEY
from args.meta_arg import MetaArg
from args.arg import Arg
from args.utils import valid_time, time_less, escape_time


class MeetingTime(Arg, metaclass=MetaArg, argtype=_ArgType._MEETING_TIME):
    """Meeting Time argument."""

    @classmethod
    def _valid_input_value(cls, input_value: _InputValue) -> bool:
        input_value = input_value.split(' - ')
        if len(input_value) != 2:
            return False
        start, end = input_value
        return valid_time(start) and valid_time(end) and time_less(start, end)
    
    @classmethod
    def _prepare_input(cls, input: _RawInputValue) -> _InputValues:
        return [input]
    
    @classmethod
    def _fix_input_values(cls, input_values: _InputValues) -> _InputValues:
        if not cls._valid_input_value(input_values[0]):
            cls._print_invalid_input_values_msg(input_values)
            return []
        
        start, end = input_values[0].split(' - ')
        return [escape_time(start), escape_time(end)]
    
    @classmethod
    def _make_kvpairs(cls, query_values: _QueryValues) -> _QueryKVPairs:
        if not query_values:
            return []

        return {
            (
                _ARG_TYPE_TO_QUERY_KEY[_ArgType._MEETING_TIME_START],
                (query_values[0],)
            ),
            (
                _ARG_TYPE_TO_QUERY_KEY[_ArgType._MEETING_TIME_END],
                (query_values[1],)
            )
        }
    
    @classmethod
    def _print_valid_input_values(cls) -> None:
        print('Valid Meeting Time example: 10:30 AM - 12:00 PM')
