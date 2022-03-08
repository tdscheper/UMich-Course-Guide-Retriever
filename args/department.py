"""Define class for Department argument."""
from args import _ArgType, _InputValue
from args.meta_arg import MetaArg
from args.arg import Arg


class Department(Arg, metaclass=MetaArg, argtype=_ArgType._DEPARTMENT):
    """Department argument."""

    # This is necessary since Department is a dependency for other
    # arguments (Subject, Course)
    @classmethod
    def _valid_input_value(cls, input_value: _InputValue) -> bool:
        return input_value.isalpha() and input_value.isupper() and \
            2 <= len(input_value) <= 8
