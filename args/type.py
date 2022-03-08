"""Define class for Type argument."""
from args import _ArgType, _RawInputValue, _InputValues
from args.meta_arg import MetaArg
from args.arg import Arg


class Type(Arg, metaclass=MetaArg, argtype=_ArgType._TYPE, mandatory=True):
    """Type argument."""

    @classmethod
    def _prepare_input(cls, input: _RawInputValue) -> _InputValues:
        return [input]
    
    @classmethod
    def _fix_input_values(cls, input_values: _InputValues) -> _InputValues:
        if not cls._valid_input_value(input_values[0]):
            cls._print_invalid_input_values_msg(input_values)
            return [cls._DEFAULT_INPUT_VALUE]
        return input_values
    
    @classmethod
    def _print_invalid_input_values_msg(cls, invalids: _InputValues) -> None:
        print(f"Type '{invalids[0]}' invalid or not supported.")
        cls._print_valid_input_values()
        print(f'Using {cls._DEFAULT_INPUT_VALUE}')
