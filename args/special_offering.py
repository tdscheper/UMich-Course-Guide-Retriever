"""Define class for Special Offering argument."""
from args import _ArgType
from args.meta_arg import MetaArg
from args.arg import Arg


class SpecialOffering(Arg, metaclass=MetaArg, 
                      argtype=_ArgType._SPECIAL_OFFERING):
    """Special Offering argument."""

    pass  # Default good
