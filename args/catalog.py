"""Define class for Catalog argument."""
from args import _ArgType, _InputValue
from args.meta_arg import MetaArg
from args.arg import Arg


class Catalog(Arg, metaclass=MetaArg, argtype=_ArgType._CATALOG):
    """Catalog argument."""

    # This is necessary since Catalog is a dependency for another
    # argument (Course)
    @classmethod
    def _valid_input_value(cls, input_value: _InputValue) -> bool:
        return input_value.isdigit() and 100 <= int(input_value) <= 999
