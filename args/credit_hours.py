"""Define class for Credit Hours argument."""
from args import _ArgType
from args.meta_arg import MetaArg
from args.arg import Arg


class CreditHours(Arg, metaclass=MetaArg, argtype=_ArgType._CREDIT_HOURS):
    """Credit Hours argument."""

    pass  # Default good
