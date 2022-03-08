"""Define class for Distribution Requirement argument."""
from args import _ArgType
from args.meta_arg import MetaArg
from args.arg import Arg


class DistributionReq(Arg, metaclass=MetaArg, 
                      argtype=_ArgType._DISTRIBUTION_REQUIREMENT):
    """Distribution Requirment argument."""

    pass  # Default good
