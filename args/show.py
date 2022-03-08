"""Define class for Show argument."""
from args import _ArgType
from args.meta_arg import MetaArg
from args.arg import Arg


class Show(Arg, metaclass=MetaArg, argtype=_ArgType._SHOW, mandatory=True):
    """Show argument."""

    pass  # Nothing to do
