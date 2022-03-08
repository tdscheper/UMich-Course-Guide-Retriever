"""Define class for Meeting Time End argument."""
from args import _ArgType, _InputValue
from args.meta_arg import MetaArg
from args.arg import Arg
from args.utils import valid_time


class MeetingTimeEnd(Arg, metaclass=MetaArg, 
                     argtype=_ArgType._MEETING_TIME_END):
    """Meeting Time End argument."""

    @classmethod
    def _valid_input_value(cls, input_value: _InputValue) -> bool:
        return valid_time(input_value)
