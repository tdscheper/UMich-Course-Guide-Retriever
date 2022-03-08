"""Define class for Page Number argument."""
from args import _ArgType
from args.meta_arg import MetaArg
from args.arg import Arg


class PageNumber(Arg, metaclass=MetaArg, argtype=_ArgType._PAGE_NUMBER,
                 mandatory=True):
    """Page Number argument."""

    pass  # Nothing to do
