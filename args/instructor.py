"""Define class for Instructor argument."""
from args import _ArgType, _InputValue, _RawInputValue, _InputValues
from args.meta_arg import MetaArg
from args.arg import Arg


class Instructor(Arg, metaclass=MetaArg, argtype=_ArgType._INSTRUCTOR):
    """Instructor argument."""

    @classmethod
    def _valid_input_value(cls, input_value: _InputValue) -> bool:
        # Valid input value is a valid uniqname
        # Valid uniqname is 3-8 letters
        return input_value.isalpha() and 3 <= len(input_value) <= 8
    
    @classmethod
    def _prepare_input(cls, input: _RawInputValue) -> _InputValues:
        return [input]
    
    @classmethod
    def _print_invalid_input_values_msg(cls, invalids: _InputValues) -> None:
        print(f"Not using invalid Instructor '{invalids[0]}'")
        cls._print_valid_input_values()
    
    @classmethod
    def _print_valid_input_values(cls) -> None:
        print(f'A valid Instructor is a valid uniqname.')
