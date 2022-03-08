"""
Define class for Other Requirement argument.
Skills Requirement and Special Offering arguments are Other Requirement
arguments.
"""
from args import _ArgType
from args.meta_arg import MetaArg
from args.arg import Arg


class OtherReq(Arg, metaclass=MetaArg, argtype=_ArgType._OTHER_REQUIREMENT):
    """Other Requirement argument."""

    pass  # Nothing to do
